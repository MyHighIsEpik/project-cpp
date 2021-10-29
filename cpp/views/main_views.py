from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.utils import redirect
from cpp.forms import UserLoginForm
from werkzeug.security import check_password_hash
from cpp.models import User
from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


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
            return redirect(url_for('program.program'))
        flash(error)
    return render_template('auth/mainpage.html', form=form)
