# http://localhost:8070/testGet?a=11&b=13
# from flask import Flask, request, jsonify
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/testGet', methods=["GET"])
def calculateGet():
    print(request)
    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    c = int(a) + int(b)
    res = {"result": c}
    return jsonify(content_type='application/json;charset=utf-8',
                   reason='success',
                   charset='utf-8',
                   status='200',
                   content=res)


@app.route('/testPost', methods=["POST"])
def calculatePost():
    params = request.form if request.form else request.json
    print(params)
    a = params.get("a", 0)
    b = params.get("b", 0)
    c = a + b
    res = {"result": c}
    return jsonify(content_type='application/json;charset=utf-8',
                   reason='success',
                   charset='utf-8',
                   status='200',
                   content=res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=False, port=8070)