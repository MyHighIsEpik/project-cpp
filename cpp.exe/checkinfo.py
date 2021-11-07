import platform
import psutil
import shutil
import subprocess

# platfrom 라이브러리 이용해서 os 버전과 이름 파악
def OsInfo():
    global os_name, os_version
    os_name = platform.system()
    os_version = platform.version()
    full_osversion = os_version
    os_version = os_version.split('.')
    os_version = os_version[0]

    return os_version, full_osversion


# psutil 라이브러리 이용해서 RAM 크기 파악 후 GB로 출력
def RAMInfo():
    global ram_size
    ram_size = round(psutil.virtual_memory().total / (10 ** 9))
    return ram_size


# subprocess사용 cpu 정보 구하기
def CPUInfo():
    global cpu_info
    cmd = ['wmic', 'cpu', 'list', 'brief/format:list']                                  # 스페이스를 기준으로 명령어를 잘라서 list로 만듦
    fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout                     # 명령어 실행 후 반환되는 결과를 파일에 저장
    datafile = fd_popen.read().strip()                                                  # 파일에서 저장된 결과를 읽어 data에 저장
    fd_popen.close()                                                                    # 파일 닫기
    datafile = datafile.decode()                                                        # cpu_info = cpu 사양 페이지 출력 변수
    cpu_info = datafile.split('\r\r\n')[4]
    cpu_info = cpu_info.replace("Name=", "")                                            # cpu_info1 = cpu 사양비교 변수
    if 'Core' in cpu_info or 'Atom' in cpu_info:                                        # case1 : 내 PC의 CPU가 intel core, atom일 떄
        cpu_info = cpu_info.replace('(R)', '').replace('(TM)', '').replace('CPU ', '')  # 검색이 용이하도록 일부 문자열 제거
    elif 'Xeon' in cpu_info or 'Celeron' in cpu_info or 'Pentium' in cpu_info:          # case1 : 내 PC의 CPU가 intel xeon, celeron, pentium일 떄
        h = cpu_info.replace('(R)', '').replace('CPU ', '')                             # 검색이 용이하도록 일부 문자열 제거
    return cpu_info


# subprocess사용 그래픽카드 정보 구하기
def VideoInfo():
    global video_info, video_info1, video_info2
    cmd = ['wmic', 'path', 'win32_VideoController', 'get', 'name']                      # 스페이스를 기준으로 명령어를 잘라서 list로 만듦
    fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout                     # 명령어 실행 후 반환되는 결과를 파일에 저장
    video_info = fd_popen.read().strip()
    fd_popen.close()                                                                    # 파일 닫기
    video_inf = video_info.decode()                                                     # video_info = 그래픽카드 페이지 출력 변수
    video_info = video_inf.split('\n')[1]                                               # video_info1 = 그래픽카드 사양비교 변수
    video_info = video_info.split()
    del video_info[0]                                                                   # 제조사 부분 제거
    video_info = (' ').join(video_info)
    return video_info


def VideoInfo2():
    global video_info, video_info1, video_info2
    cmd = ['wmic', 'path', 'win32_VideoController', 'get', 'name']                      # 스페이스를 기준으로 명령어를 잘라서 list로 만듦
    fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout                     # 명령어 실행 후 반환되는 결과를 파일에 저장
    video_info = fd_popen.read().strip()
    fd_popen.close()                                                                    # 파일 닫기
    video_inf = video_info.decode()                                                     # video_info = 그래픽카드 페이지 출력 변수
    video_info = video_inf.split('\n')[1]                                               # video_info1 = 그래픽카드 사양비교 변수
    video_info = video_info.split()
    del video_info[0]                                                                   # 제조사 부분 제거
    video_info = (' ').join(video_info)
    # 두 번째 그래픽카드가 있을 경우
    try:
        video_info1 = video_inf.split('\n')[2]
        video_info1 = video_info1.split()
        del video_info1[0]
        video_info1 = (' ').join(video_info1)
        return video_info1
    except IndexError:
        print("인덱싱 할 수 없습니다.")


# shutil 라이브러리 이용해서 Disk 정보 파악 후 MB로 변환
def DiskInfo():
    global disklist, c_free, d_free, e_free, f_free
    diskLabel = 'c:\\'
    diskLabel2 = 'd:\\'
    diskLabel3 = 'e:\\'
    diskLabel4 = 'f:\\'
    disklist = []

    try:
        c_free = round(shutil.disk_usage(diskLabel).free / (10 ** 6))
        disklist.append(c_free)
    except:
        c_free = 0
        disklist.append(c_free) 
    try:
        d_free = round(shutil.disk_usage(diskLabel2).free / (10 ** 6))
        disklist.append(d_free)
    except:
        d_free = 0
        disklist.append(d_free)
    try:
        e_free = round(shutil.disk_usage(diskLabel3).free / (10 ** 6))
        disklist.append(e_free)
    except:
        e_free = 0
        disklist.append(e_free)
    try:
        f_free = round(shutil.disk_usage(diskLabel4).free / (10 ** 6))
        disklist.append(f_free)
    except:
        f_free = 0
        disklist.append(f_free)

    return disklist

