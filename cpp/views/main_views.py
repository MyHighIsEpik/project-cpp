from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.utils import redirect
from ..forms import UserLoginForm
from werkzeug.security import check_password_hash
from ..models import User, Question, Answer, question_voter
from ..views.auth_views import login_required
from sqlalchemy import func
from .. import db

bp = Blueprint('main', __name__, url_prefix='/')



@bp.route('/')
def index():
    return redirect(url_for('main.main'))


@bp.route('/mainpage/', methods=('GET', 'POST'))
def main():
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
    return render_template('auth/mainpage.html', form=form)

@bp.route('/homepage/')
@login_required
def homepage():
    return render_template('/homepage.html')

