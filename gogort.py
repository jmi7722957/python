from operator import le
import os
import re
import time
from tokenize import Double
import urllib.request
from warnings import catch_warnings

# 填写下面的参数   
headName="http://www.9090gort.net"#地址头
url="http://www.9090gort.net/html/yazhou/8912.html"#全地址
tempUrl=""

def get_htmls(url):
    page = urllib.request.urlopen(url)
    html_a = page.read()
    return html_a.decode('GBK')

def get_list(html):
    #获取图片所在div
    # div_reg = r'<div class="main">(.*)</div>'
    # div_regBean = re.compile(div_reg)
    # divList = div_regBean.findall(html)
    html=html.replace('\n','')
    html=html.replace('\r','')
    html=str.lower(html)
    html=re.sub(r"<!--.*?-->","",html)

    #开始解析套图标题
    title_reg = r'<div class=\'content_title\'>(.{1,30})</div>'
    title_regBean = re.compile(title_reg)
    titlelist=title_regBean.findall(html)
    title=titlelist[0]

    # print(nameHtml)
    #开始解析真图片名字
    name_reg = r'alt="'+title+'" src=\"http://.*?/.*?/.*?/.*?/.*?/(.*?)\.jpg\"'
    name_regBean = re.compile(name_reg)
    namelist=name_regBean.findall(html)
    for name in namelist:
        print(name)

    #开始解析真图片url
    url_reg = r'alt="'+title+'" src=\"(http://.*?/.*?/.*?/.*?/.*?/.*?\.jpg)\"'
    url_regBean = re.compile(url_reg)
    urllist=url_regBean.findall(html)
    # for url in urllist:
    #     print(url)

    # 打开imgList,下载图片到本地
    for index in range(len(urllist)):
        try:
            # title="乔依琳2"#保存文件夹
            path = 'E:\\'+title  # 设置图片的保存地址
            if not os.path.isdir(path):
                os.makedirs(path)  # 判断没有此路径则创建
            paths = path + '\\'  # 保存在test路径下
            urllib.request.urlretrieve(urllist[index], '{0}{1}.jpg'.format(paths,namelist[index]))
        except BaseException:
            print("下载失败!!!!!!!!!!:",urllist[index])   

    #获取地址尾
    btn_reg = r'href=\"(/html/.{1,50}\.html)\">下一页</a>'
    btn_regBean = re.compile(btn_reg)
    nextPageList = btn_regBean.findall(html)
    # print(headName+nextPageList[0])

    tempNextPage=nextPageList[0]
    nextUrl=headName+nextPageList[0]
    papapa(nextUrl)

def papapa(url):
    print(url)
    global tempUrl
    global time_end
    if tempUrl==url:
        print("下载完成!!!100%请享用!!!")
        time_end = time.time()
        time_c= time_end - time_start   #运行所花时间
        print('总耗时:', round(time_c/60,2),'min')#四舍五入
        return
    tempUrl=url
    htmlText=get_htmls(url)
    get_list(htmlText)

time_start = time.time() #开始计时 
papapa(url)
