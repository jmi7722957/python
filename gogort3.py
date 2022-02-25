import os
import time
import asyncio
import requests

title="留学生小婵"#保存文件夹
path = 'E:\\'+title  # 设置图片的保存地址
if not os.path.isdir(path):
     os.makedirs(path)  # 判断没有此路径则创建
paths = path + '\\'  # 保存在test路径下

url="http://p.9090gort.net/uploadfile/2020/1116/07/01.jpg"
head=url[0:46]

def papapa(url):
    time_start = time.time()
    for index in range(1,500):
        name=""
        if index<10:
            name="0"+str(index)
        else:
            name=str(index)
        try:
            urlStr=head+name+".jpg"
            pathStr=paths+name+".jpg"
            r = requests.get(urlStr)
            # with open(pathStr,"wb") as code:
            #     code.write(r.content)
            if r.reason=='OK':
                file=open(pathStr,"wb")
                file.write(r.content)
                print(pathStr)
            else:
                time_end = time.time()
                costTime=time_end-time_start
                print('总耗时:', round(costTime/60,2),'min')#四舍五入
                print("已下载全部:",pathStr)
                file.close()#用完记得关闭清缓存
                return 
        except BaseException:
            print('下载失败!!!请检查程序')

papapa(url)

   

