import configparser
config=configparser.ConfigParser()#相当于创建一个空字典
# print(config)
config['DEFAULT']={'serverAliveinterval':45,'compresion':'yes','compressionLevel':'9'}
config['www.baidu.com']={}
topsecret=config['www.baidu.com']
topsecret['host port']='50022'
topsecret['forwardxll']='no'
config.add_section('yuan')#新增一个块
config.set('yuan','k1','1111')#增加一个键值对
# config.remove_section('www.baidu.com')#删除块（包括块下的键值会一起删除）
# config.remove_option('www.baidu.com','host port')#删除块下的件（包括值)
# with open('example.ini','w') as f: #将字典写入文件中
#     config.write(f)
# for key in config['www.baidu.com']:#便利其它块的键后会便利DEFAULT块的键
#     print(key)
# print(config.options('www.baidu.com'))#取块下的键放入列表中,包括DEFAULT块的键
# print(config.items('www.baidu.com'))#取块下的键与值组合到元组里，包括DEFAULT块的键与值
# print(config.get('www.baidu.com','host port'))#取块下键对应的值