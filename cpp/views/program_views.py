from datetime import datetime
from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect
from sqlalchemy import func

from .. import db
from ..models import Cadinfo, Gameinfo, Illustinfo

bp = Blueprint('program', __name__, url_prefix='/program')


@bp.route('/')
def program():
    return render_template('program/program.html')


@bp.route('/cad_list/')
def cad():
    # 입력 파라미터
    kw = request.args.get('kw', type=str, default='')

    cad_list = Cadinfo.query.order_by(Cadinfo.id)
    # 조회
    if kw:
        search = '%%{}%%'.format(kw)
        cad_list = cad_list \
            .filter(Cadinfo.subject.ilike(search)   # 질문제목
                    ) \
            .distinct()
    return render_template('program/cad_list.html', cad_list=cad_list, kw=kw)


@bp.route('/cad_list/detail/<int:cad_id>/')
def cad_detail(cad_id):
    cadinfo = Cadinfo.query.get_or_404(cad_id)
    return render_template('program/cad_detail.html', cadinfo=cadinfo)


@bp.route('/game_list/')
def game():
    # 입력 파라미터
    kw = request.args.get('kw', type=str, default='')

    game_list = Gameinfo.query.order_by(Gameinfo.id)
    # 조회
    if kw:
        search = '%%{}%%'.format(kw)
        game_list = game_list \
            .filter(Gameinfo.subject.ilike(search)   # 질문제목
                    ) \
            .distinct()
    return render_template('program/game_list.html', game_list=game_list, kw=kw)


@bp.route('/game_list/detail/<int:game_id>/')
def game_detail(game_id):
    gameinfo = Gameinfo.query.get_or_404(game_id)
    return render_template('program/game_detail.html', gameinfo=gameinfo)


@bp.route('/illust_list/')
def illust():
    # 입력 파라미터
    kw = request.args.get('kw', type=str, default='')

    illust_list = Illustinfo.query.order_by(Illustinfo.id)
    # 조회
    if kw:
        search = '%%{}%%'.format(kw)
        illust_list = illust_list \
            .filter(Illustinfo.subject.ilike(search)   # 질문제목
                    ) \
            .distinct()
    return render_template('program/illust_list.html', illust_list=illust_list, kw=kw)


@bp.route('/illust_list/detail/<int:illust_id>/')
def illust_detail(illust_id):
    illustinfo = Illustinfo.query.get_or_404(illust_id)
    return render_template('program/illust_detail.html', illustinfo=illustinfo)

