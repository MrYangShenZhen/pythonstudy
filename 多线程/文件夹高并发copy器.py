import os
import multiprocessing

def copy_file(file_name,source_dir,dest_dir):
    source_path=source_dir+"/"+file_name
    dest_path=dest_dir+"/"+file_name

    with open(source_path,"rb") as source_file:
        with open(dest_path,"wb")as dest_file:
            while True:
                data=source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break

if __name__=='__main__':
    source_dir=r"F:\标准版需求\新标准版\Curl"
    dest_dir=r"F:\标准版需求\新标准版\test"
    #2.创建目标文件夹
    try:
        os.makedirs(dest_dir)
    except:
        print("文件夹已存在")

    #读取源文件夹的文件列表
    file_list=os.listdir(source_dir)
    for file_name in file_list:
        # copy_file(file_name,source_dir,dest_dir)
        sub_process=multiprocessing.Process(target=copy_file,args=(file_name,source_dir,dest_dir))
        sub_process.start()
