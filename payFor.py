import os
import webbrowser

path=os.getcwd()#获取当地路径
url = "http://localhost:8066/api/getPyFor"
# 自动打开浏览器
webbrowser.open("http://localhost:8066/PyFor.html?root="+path)
