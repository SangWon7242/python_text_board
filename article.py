import user as u

class Article():
    def __init__(self, id, title, body, writer_name):
        self.id = id
        self.title = title
        self.body = body
        self.writer_name = writer_name
        
    def __str__(self):
        return "id : {}, title : \"{}\", body : \"{}\", writer_name : {}".format(self.id, self.title, self.body, self.writer_name)

article_list = []  # 게시물 저장소

last_no = len(article_list)

# 테스트 데이터
def make_test_data(article_list = article_list):    
    for i in range(1, 6):
        id = i
        article_list.append(Article(id, "제목" + str(id), "내용" + str(id), "작성자" + str(id)))
                                        
make_test_data()

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
    
    id = last_no            
    last_no += 1

    article = Article(id, title, body, name)

    print("게시물이 등록 되었습니다.")
    print("등록 된 게시물 : {}".format(article))
    article_list.append(article)
    


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
    id = int(input("상세보기 할 게시물 번호 입력 : "))
    
    if not article_list:
        print("게시물이 존재하지 않습니다.")
        return        
    
    for article in article_list:
        if article.id == id:            
            print("==========  게시물 상세보기  =========")
            print("번호 : ", article.id)
            print("제목 : ", article.title)
            print("내용 : ", article.body)
            print("작성자 : ", article.writer_name)
            print("=================================")                                
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