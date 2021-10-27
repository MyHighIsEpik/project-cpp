import string
import random

class giverandomcode():
    new_pw_len = 10  # 새 비밀번호 길이

    pw_candidate = string.ascii_letters + string.digits

    randomcode = ""
    for i in range(new_pw_len):
        randomcode += random.choice(pw_candidate)
