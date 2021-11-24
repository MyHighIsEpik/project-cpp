from datetime import datetime
from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect

from .. import db
from ..forms import AnswerForm
from ..models import Question, Answer, User, User_pcinfo, Cpulist, Videocard
from .auth_views import login_required

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
@login_required
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now(), user=g.user, user_codenum=g.user.codenum)
        question.answer_set.append(answer)
        db.session.commit()
        return redirect('{}#answer_{}'.format(
            url_for('question.detail', question_id=question_id), answer.id))
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def modify(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    if g.user != answer.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', question_id=answer.question.id))
    if request.method == "POST":
        form = AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(answer)
            answer.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect('{}#answer_{}'.format(
                url_for('question.detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(obj=answer)
    return render_template('answer/answer_form.html', answer=answer, form=form)

@bp.route('/delete/<int:answer_id>')
@login_required
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    question_id = answer.question.id
    if g.user != answer.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))

@bp.route('/question/detail/<int:answer_id>/compare/')
@login_required
def answer_compare(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    # 게시글 작성자
    answerer = User.query.filter_by(id=answer.user_id).first()
    answerer_pcinfo = User_pcinfo.query.filter_by(codenum=answerer.codenum).first()
    answerer_cpu = Cpulist.query.filter_by(cpuname=answerer_pcinfo.cpu).first()
    answerer_video = Videocard.query.filter_by(vcname=answerer_pcinfo.graphic1).first()
    # 현재 사용자
    user_pcinfo = User_pcinfo.query.filter_by(codenum=g.user.codenum).first()
    user_cpu = Cpulist.query.filter_by(cpuname=user_pcinfo.cpu).first()
    a = '%' + user_pcinfo.graphic1 + '%'
    user_video = Videocard.query.filter(Videocard.vcname.like(a)).first()

    return render_template('answer/answer_compare.html', \
                           answerer_pcinfo=answerer_pcinfo, answerer_cpu=answerer_cpu, \
                           answerer_video=answerer_video, user_pcinfo=user_pcinfo, user_cpu=user_cpu, \
                           user_video=user_video)
