from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.utils import redirect
from ..forms import UserLoginForm
from werkzeug.security import check_password_hash
from ..models import User, User_pcinfo, Question, Answer, question_voter
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
    user_pcinfo = User_pcinfo.query.filter_by(codenum=g.user.codenum).first()

    # 정렬
    # 추천많은글
    sub_query = db.session.query(question_voter.c.question_id, func.count('*').label('num_voter')) \
        .group_by(question_voter.c.question_id).subquery()
    question_list1 = Question.query \
        .outerjoin(sub_query, Question.id == sub_query.c.question_id) \
        .order_by(sub_query.c.num_voter.desc(), Question.create_date.desc())
    # 댓글많은글
    sub_query = db.session.query(Answer.question_id, func.count('*').label('num_answer')) \
        .group_by(Answer.question_id).subquery()
    question_list2 = Question.query \
        .outerjoin(sub_query, Question.id == sub_query.c.question_id) \
        .order_by(sub_query.c.num_answer.desc(), Question.create_date.desc())
    # 최신글
    question_list3 = Question.query.order_by(Question.create_date.desc())

    return render_template('/homepage.html', question_list1=question_list1, question_list2=question_list2, \
                           question_list3=question_list3, user_pcinfo=user_pcinfo)
