user1 = {"아이디": "hong123", "비밀번호": "1234", "이름": "홍길동"}
user2 = {"아이디": "sony7", "비밀번호": "7777", "이름": "손흥민"}
user3 = {"아이디": "ryu99", "비밀번호": "9999", "이름": "류현진"}

user_list = [user1, user2, user3]  # 회원 저장소

user_last_no = len(user_list)

def get_member_login_id(login_id):
    for user in user_list:
        if user["아이디"] == login_id:
            return user["아이디"]

    return False

def get_member_login_pw(login_pw):
    for user in user_list:
        if user["비밀번호"] == login_pw:
            return user["비밀번호"]

    return False

def do_join():
    login_id = input("로그인 아이디 : ")
    
    if get_member_login_id(login_id) == login_id:
        print("id가 중복 되었습니다.")
        return
    
    login_pw = input("로그인 비밀번호 : ")
    login_pw_confirm = input("로그인 비밀번호 확인 : ")
    
    if login_pw != login_pw_confirm:
        print("비밀번호가 일치하지 않습니다.")
        return
    
    name = input("이름을 입력해주세요 : ")
    
    user = {"아이디": login_id, "비밀번호": login_pw, "이름": name}

    print("{}님. 가입을 환영합니다.".format(login_id))
    user_list.append(user)    
        
def login_chcked(login_id, login_pw):
    check_login_id = get_member_login_id(login_id)

    if check_login_id == False:
        print("아이디를 잘 못 입력하셨습니다.")
        return

    check_login_pw = get_member_login_pw(login_pw)

    if check_login_pw == False:
        print("비밀번호를 잘 못 입력하셨습니다.")
        return

    print("{}님 환영합니다.".format(login_id))
    return True