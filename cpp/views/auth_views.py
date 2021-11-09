import functools
from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from cpp import db
from cpp.forms import UserCreateForm, UserLoginForm, UserDeleteForm
from cpp.models import User, User_pcinfo
from cpp.randomcode import giverandomcode

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        nickname=form.nickname.data, codenum=giverandomcode.randomcode)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.homepage'))
        flash(error)
    return render_template('auth/login.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

    #여기서 g.user에 로그인 한 유저의 정보값이 들어감

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:          #로그인 한 상태가 아니라면 첫 페이지로 이동
            return redirect(url_for('main.index'))
        return view(**kwargs)
    return wrapped_view

@bp.route('/mypage/')
@login_required
def mypage():
    user_pcinfo = User_pcinfo.query.filter_by(codenum=g.user.codenum).first()
    return render_template('auth/mypage.html', user_pcinfo=user_pcinfo)


@bp.route('/mypage/quit/', methods=('GET', 'POST'))
def quit():
    form = UserDeleteForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(codenum=form.codenum.data).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('코드가 일치하지 않습니다.')
    return render_template('auth/quit.html', form=form)
