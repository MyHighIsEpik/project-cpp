from flask import Blueprint, request, render_template, g
from flask import send_file

from .. import db
from ..models import Cadinfo, Gameinfo, Illustinfo, User_pcinfo, Cpulist, Videocard
from ..views.auth_views import login_required

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
            .filter(Cadinfo.name.ilike(search)   # 질문제목
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
            .filter(Gameinfo.name.ilike(search)   # 질문제목
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
            .filter(Illustinfo.name.ilike(search)   # 질문제목
                    ) \
            .distinct()
    return render_template('program/illust_list.html', illust_list=illust_list, kw=kw)


@bp.route('/illust_list/detail/<int:illust_id>/')
def illust_detail(illust_id):
    illustinfo = Illustinfo.query.get_or_404(illust_id)
    return render_template('program/illust_detail.html', illustinfo=illustinfo)

@bp.route('/download/')
def download():
    file_name = f"static/exe/programgui.exe"
    return send_file(file_name,
                     mimetype='application/octet-stream',
                     as_attachment=True,
                     attachment_filename='CPP.exe')

# 사양비교

@bp.route('/cad_list/detail/<int:cad_id>/compare/')
@login_required
def cad_compare(cad_id):
    # 프로그램 사양
    cadinfo = Cadinfo.query.get_or_404(cad_id)
    cadcpu = Cpulist.query.filter_by(cpuname=cadinfo.cpu).first()
    cadvideo = Videocard.query.filter_by(vcname=cadinfo.videocard).first()
    cadinfo_os = cadinfo.osversion.split('.')
    cadinfo_os = cadinfo_os[0]
    # 현재 사용자
    user_pcinfo = User_pcinfo.query.filter_by(codenum=g.user.codenum).first()
    usercpu = Cpulist.query.filter_by(cpuname=user_pcinfo.cpu).first()
    # uservideo = Videocard.query.filter_by(vcname=user_pcinfo.graphic1).first()
    a = '%' + user_pcinfo.graphic1 +'%'
    uservideo = Videocard.query.filter(Videocard.vcname.like(a)).first()

    return render_template('program/cad_compare.html', \
                           cadinfo=cadinfo, cadcpu=cadcpu, cadvideo=cadvideo, cadinfo_os=cadinfo_os, \
                           user_pcinfo=user_pcinfo, usercpu=usercpu, uservideo=uservideo)


@bp.route('/game_list/detail/<int:game_id>/compare/')
@login_required
def game_compare(game_id):
    # 프로그램 사양
    gameinfo = Gameinfo.query.get_or_404(game_id)
    gamecpu = Cpulist.query.filter_by(cpuname=gameinfo.cpu).first()
    gamevideo = Videocard.query.filter_by(vcname=gameinfo.videocard).first()
    gameinfo_os = gameinfo.osversion.split('.')
    gameinfo_os = gameinfo_os[0]
    # 현재 사용자
    user_pcinfo = User_pcinfo.query.filter_by(codenum=g.user.codenum).first()
    usercpu = Cpulist.query.filter_by(cpuname=user_pcinfo.cpu).first()
    # uservideo = Videocard.query.filter_by(vcname=user_pcinfo.graphic1).first()
    a = '%' + user_pcinfo.graphic1 +'%'
    uservideo = Videocard.query.filter(Videocard.vcname.like(a)).first()

    return render_template('program/game_compare.html', \
                           gameinfo=gameinfo, gamecpu=gamecpu, gamevideo=gamevideo, gameinfo_os=gameinfo_os, \
                           user_pcinfo=user_pcinfo, usercpu=usercpu, uservideo=uservideo)


@bp.route('/illust_list/detail/<int:illust_id>/compare/')
@login_required
def illust_compare(illust_id):
    # 프로그램 사양
    illustinfo = Illustinfo.query.get_or_404(illust_id)
    illustcpu = Cpulist.query.filter_by(cpuname=illustinfo.cpu).first()
    illustvideo = Videocard.query.filter_by(vcname=illustinfo.videocard).first()
    illustinfo_os = illustinfo.osversion.split('.')
    illustinfo_os = illustinfo_os[0]
    # 현재 사용자
    user_pcinfo = User_pcinfo.query.filter_by(codenum=g.user.codenum).first()
    usercpu = Cpulist.query.filter_by(cpuname=user_pcinfo.cpu).first()
    # uservideo = Videocard.query.filter_by(vcname=user_pcinfo.graphic1).first()
    a = '%' + user_pcinfo.graphic1 +'%'
    uservideo = Videocard.query.filter(Videocard.vcname.like(a)).first()

    return render_template('program/illust_compare.html', \
                           illustinfo=illustinfo, illustvideo=illustvideo, illustcpu=illustcpu, \
                           illustinfo_os=illustinfo_os, user_pcinfo=user_pcinfo, usercpu=usercpu, uservideo=uservideo)


