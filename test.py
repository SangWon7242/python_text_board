class Article():
    def __init__(self, id, title, body, writer_name):
        self.id = id
        self.title = title
        self.body = body
        self.writer_name = writer_name
        
    def __str__(self):
        return "id : {}, title : \"{}\", body : \"{}\", writer_name : \"{}\"".format(self.id, self.title, self.body, self.writer_name)

article_list = []

def make_test_data(article_list = article_list):    
    for i in range(1, 6):
        id = i
        article_list.append(Article(id, "제목" + str(id), "내용" + str(id), "작성자" + str(id)))
                                        
make_test_data()

for article in article_list:
    print(article.id)
    print(article.title)