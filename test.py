class Article():
    def __init__(self, id, title, body, writer_name):
        self.id = id
        self.title = title
        self.body = body
        self.writer_name = writer_name
        
    def __str__(self):
        return "id : {}, title : \"{}\", body : \"{}\", writer_name : {}".format(self.id, self.title, self.body, self.writer_name)

article = Article(1, "제목1", "내용1", "홍길동")

print(article)
print(article.id)
print(article.title)
print(article.body)