from flask import g
from models import Cadinfo, Gameinfo, Illustinfo, User_pcinfo, Cpulist
from views.program_views import cad_compare


cadinfo = cad_compare()
user_pcinfo = User_pcinfo.query.filter_by(codenum=g.user.codenum).first()
programcpuinfo = Cpulist.query.filter_by(cpuname=cadinfo.cpu)
usercpuinfo = Cpulist.query.filter_by(cpuname=user_pcinfo.cpu)

def compare_cpu():
    if programcpuinfo.score < usercpuinfo.score :
        return False
    else :
        return True


