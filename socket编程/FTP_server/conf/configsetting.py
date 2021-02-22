import  configparser
config = configparser.ConfigParser()
config["DEFAULT"] = {}
config.read('Account.org')
config['admin']={'password':'000000','Quotation':'100'}
with open('Account.org','w') as f: #将字典写入文件中
    config.write(f)