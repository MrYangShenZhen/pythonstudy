# 假设每本书只有一本

class Book(object):
    def __init__(self, name, author, state, bookIndex):
        self.name = name
        self.author = author
        # 0：'已借出' 1:'未借出'
        self.state = state
        self.bookIndex = bookIndex


    def __str__(self):
        return  'Book(%s, %d)' %(self.name, self.state)

class   BookManage(object):
    # 存放所有书籍信息, 列表里面存放的是Book对象
    books = []

    def start(self):
        """图书管理系统初始化数据"""
        self.books.append(Book('python', 'Guido', 1, 'IN23445'))
        self.books.append(Book('java', 'Guido1', 1, 'IN23445'))
        self.books.append(Book('C++', 'Guido2', 1, 'IN23445'))
        print("初始化数据成功!")

    def Menu(self):
        """图书管理菜单栏"""
        while True:
            print("""
                        图书管理操作
                        
            1). 添加书籍
            2). 删除数据
            3). 查询书籍
            4). 退出
            """)
            choice = input("请输入你的选择:")
            if choice == '1':
                self.addBook()
            elif choice == '2':
                self.delBook()
            elif choice == '3':
                self.borrowBook()
            elif choice == '4':
                exit()
            else:
                print("请输入正确的选择!")

    def addBook(self):
        print("添加书籍".center(0, '*'))
        name = input("书籍名称:")
        bObj = self.isBookExist(name)
        if bObj:
            print("书籍%s已经存在" %(bObj.name))
        else:
            self.books.append(Book(name,input("作者:"), 1, input("存放位置:")))
            print("书籍%s添加成功" %(name))

    def delBook(self):
        print("删除书籍".center(50,'*'))
        for i in self.books:
            print(i)
        name = input("删除书籍名称：")
        a = self.isBookExist(name)
        if a:
            self.books.remove(a)
            print("删除%s成功" %(a))
        else:
            print("书籍不存在")

    def borrowBook(self):
        print("查询书籍".center(50,'*'))
        for i in self.books:
            print(i)
        name = input("查询书籍名称：")
        b = self.isBookExist(name)
        for book in self.books:
            if book == b:
                print(book)
                break
            else:
                print("%s不存在" %(b))
                break
    def isBookExist(self, name):
        """检测书籍是否存在"""
        # 1. 依次遍历列表books里面的每个元素
        # 2. 如果有一个对象的书名和name相等， 那么存在；
        # 3. 如果遍历所有内容， 都没有发现书名与name相同， 书籍不存在;
        for book in self.books:
            if book.name == name:
                # 因为后面需要
                return book
        else:
            return  False

if __name__ == "__main__":
    bManger = BookManage()
    bManger.start()
    bManger.Menu()