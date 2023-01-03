import user as u

class Article():
    def __init__(self, id, title, body, writer_name):
        self.id = id
        self.title = title
        self.body = body
        self.writer_name = writer_name
        
    def __str__(self):
        return "id : {}, title : \"{}\", body : \"{}\", writer_name : {}".format(self.id, self.title, self.body, self.writer_name)


article1 = {"번호": 1, "제목": "소니의 축구교실", "내용": "소니의 축구 강좌", "작성자": "sony7"}
article2 = {"번호": 2, "제목": "류뚱의 야구교실", "내용": "류뚱의 야구 강좌", "작성자": "ryu99"}
article3 = {"번호": 3, "제목": "길동의 도술교술", "내용": "길동의 도술 강좌", "작성자": "hong123"}

article_list = [article1, article2, article3]  # 게시물 저장소

last_no = len(article_list)

# ======== board 관련 함수 ==========
def help_list():
    print("exit : 게시판 종료")
    print("help : 도움말")
    print("add : 게시물 추가")
    print("list : 게시물 목록 조회")


def do_add(login_id):
    global last_no

    title = input("제목 : ")
    body = input("내용 : ")

    for user in u.user_list:
        if user["아이디"] == login_id:
            name = user["아이디"]

    article = {"번호": last_no + 1, "제목": title, "내용": body, "작성자": name}

    print("게시물이 등록 되었습니다.")
    article_list.append(article)
    last_no += 1


def show_list(split_cmd):
    order_by_desc = True
    
    if "list" in split_cmd and "asc" in split_cmd:
        order_by_desc = False
            
    print("==========  게시물 목록  =========")    
    if order_by_desc:
        for article in reversed(article_list):            
            print(
                "번호 : {}   제목 : {}  작성자 : {}".format(
                    article["번호"], article["제목"], article["작성자"]
                )
            )                  
    else:
        for article in article_list:
            print(
                "번호 : {}   제목 : {}  작성자 : {}".format(
                    article["번호"], article["제목"], article["작성자"]
                )
            )                  
    print("=================================")

def show_detail():
    ano = int(input("상세보기 할 게시물 번호 입력 : "))
    
    for article in article_list:
        if article["번호"] == ano:            
            print("==========  게시물 상세보기  =========")
            print("번호 : ", article["번호"])
            print("제목 : ", article["제목"])
            print("내용 : ", article["내용"])
            print("작성자 : ", article["작성자"])
            print("=================================")                                
            return
        
    print("없는 게시물입니다.")
    return    
            
def do_update():
    ano = int(input("수정할 게시물 번호를 입력 : "))
    
    for article in article_list:
        if article["번호"] == ano:            
            new_title = input("새 제목 : ")
            new_body = input("새 내용 : ")
            article["제목"] = new_title
            article["내용"] = new_body
            return
    
    print("없는 게시물입니다.")
    return        
            
def do_delete():
    ano = int(input("삭제할 게시물 번호를 입력 : "))
    
    for article in article_list:                
        if article["번호"] == ano:                                    
            article_list.remove(article)
            print("{}번 게시물이 삭제 되었습니다.".format(ano))                    
        
        print("없는 게시물입니다.")
        return                                        
# ======== board 관련 함수 끝 ==========

# 게시판 기능
def board_process(login_id):
    while True:
        board_cmd = input("게시판 명령어 : ")
        split_cmd = list(board_cmd.split(' '))

        if board_cmd == "help":
            help_list()

        elif board_cmd == "add":
            do_add(login_id)

        elif "list" in split_cmd:
            show_list(split_cmd)
            
        elif board_cmd == "detail":
            show_detail()              
            
        elif board_cmd == "update":
            do_update()
            
        elif board_cmd == "delete":
            do_delete()                         

        elif board_cmd == "exit":
            print("게시판 프로그램을 종료합니다.")
            break
        else:
            print("잘못 된 명령어 입니다.")