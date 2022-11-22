import re


def solution(new_id):
    length = len(new_id)

    new_id = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())  # 1단계, 2단계
    new_id = re.sub('\.\.+', '.', new_id)  # 3단계
    new_id = re.sub('^\.|\.$', '', new_id)  # 4단계

    if new_id == '':  # 5단계
        new_id = 'a'

    new_id = re.sub('\.$', '', new_id[:15])  # 6단계

    while len(new_id) <= 2:  # 7단계
        new_id += new_id[-1:]

    return new_id


solution("...!@BaT#*..y.abcdefghijklm")
