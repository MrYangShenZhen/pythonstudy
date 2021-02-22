import optparse

class Wang_opt:

    def __init__(self):
        #初始化
        parser = optparse.OptionParser()
        parser.add_option("-s", "--server", dest="server", help="ftp server ip_address")
        parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
        parser.add_option("-u", "--username", dest="username", help="username info")
        parser.add_option("-p", "--password", dest="password", help="password info")
        #解析参数
        self.options, self.args = parser.parse_args()
        print(self.options,self.args)


if __name__ == '__main__':
    whw_opt = Wang_opt()