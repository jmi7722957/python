# http://localhost:8070/testGet?a=11&b=13
# from flask import Flask, request, jsonify
import os
from queue import Empty
from re import T
import pandas as pd
from flask import Flask, request, jsonify


app = Flask(__name__)
@app.route('/getPyFor', methods=["POST"])
def calculatePost():
    # 接收参数
    params = request.form if request.form else request.json
    root = params.get("root", "")

    # path=os.getcwd()#路径
    files=os.listdir(root)#文件名
    # path=os.getcwd()

    # 利用pandas处理数据,筛选需要的图片格式
    files = pd.DataFrame(files)
    files.columns = ["name"]
    files.head()
    files = files[files.name.str.lower().str.contains("(\.jpg|jpeg|png)") == True]
    files=files.name
    files=list(files)
    # for one in files:
    #     print(one)

    #把list拆分
    l = [i for i in files]
    n = 5  #分成几个一组
    pages=[l[i:i + n] for i in range(0, len(l), n)]
        
    res = {"path": root,"FileList": files,"pages":pages}
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=False, port=8070)

calculatePost()
