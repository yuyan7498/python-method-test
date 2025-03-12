from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_request():
    # 取得請求方法
    method = request.method
    
    # 根據不同的請求方法取得資料
    if method == 'GET':
        data = dict(request.args)
    elif method in ['POST', 'PUT']:
        # 嘗試獲取 JSON 資料
        if request.is_json:
            data = request.get_json()
        # 嘗試獲取 form 資料
        elif request.form:
            data = dict(request.form)
        # 嘗試獲取 raw 資料
        else:
            data = request.get_data().decode('utf-8')
    elif method == 'DELETE':
        if request.is_json:
            data = request.get_json()
        else:
            data = dict(request.args)
    
    # 準備回應資料
    response = {
        "message": "陳彥宇好帥氣",
        "method": method,
        "data": data
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
