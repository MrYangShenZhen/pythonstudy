import logging
# logging.basicConfig(level=logging.DEBUG,filename='logger.log',filemode='w')#写的方式新建日志文件
# #日志级别
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')
# logging.basicConfig(level=logging.INFO,filename='logger01.log',format='%(lineno)d')#打印不低于info的所有日志级别到日志('w'覆盖，没有w是追加）
##format指定handler使用的日志显示格式 ,datefmt：指定日期时间格式,filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')
#format参数中可能用到的格式化串：
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s用户输出的消息
loger=logging.getLogger()
#向文件发送日志
fh=logging.FileHandler('test.log')
#向控制台发送日志
ch=logging.StreamHandler()
#设置格式对象
fm=logging.Formatter("%(asctime)s %(message)s")
#吃fm
fh.setFormatter(fm)
ch.setFormatter(fm)
#吸fh方法
loger.addHandler(fh)
#吸ch方法
loger.addHandler(ch)
loger.debug('debug 我是客家人')
loger.info('info 测试一下')