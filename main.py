import user as u
import article as a

# 실제 실행 프로그램
while True:
    cmd = input("회원가입 : join, 로그인 : login, 종료 : exit\n")

    if cmd == "join":
        u.do_join()        
        
    elif cmd == "login":
        login_id = input("아이디 : ")
        login_pw = input("비밀번호 : ")
        check = u.login_chcked(login_id, login_pw)

        if check == True:
            print("게시판 기능을 활성화 합니다.")
            a.board_process(login_id)
                

    elif cmd == "exit":
        print("프로그램을 종료합니다.")
        break