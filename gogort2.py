import os
import time
import urllib.request


url="http://p.9090gort.net/uploadfile/2020/0131/07/01.jpg"
head=url[0:46]

def papapa(url):
    time_start = time.time()
    for index in range(466,500):
        name=""
        if index<10:
            name="0"+str(index)
        else:
            name=str(index)
        try:
            title="乔依琳2"#保存文件夹
            path = 'E:\\'+title  # 设置图片的保存地址
            if not os.path.isdir(path):
                os.makedirs(path)  # 判断没有此路径则创建
            paths = path + '\\'  # 保存在test路径下
            gg=urllib.request.urlretrieve(head+name+".jpg", '{0}{1}.jpg'.format(paths,index))
            print(head+name)
        except BaseException:
            time_end = time.time()
            costTime=time_end-time_start
            print('总耗时:', round(costTime/60,2),'min')#四舍五入
            print("下载失败!!!或已下载全部:",head+name)  
            return 
    
papapa(url)
