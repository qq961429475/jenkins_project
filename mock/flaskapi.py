import json

from flask import Flask, request, jsonify

app = Flask("py44")
app.config["DEBUG"] = True
app.json.ensure_ascii = False  # 处理中文乱码

app.json.sort_keys = False  # 处理json排序


@app.route('/member/register', methods=['post'])
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    if username == 'gaofei' and password == '123456':
        return {"code": 10, "msg": "success"}
    elif username == 'gaofei' and password == '12345':
        return {"code": 20, "msg": "password error"}
    else:
        return ''


# 定义视图函数，设置路由规则
@app.route("/index", methods=['get'])  # method没有默认get
def index():
    print("欢迎访问index主页")
    return "hello mock，欢迎访问index主页"


# {"username":"test_login","password":"123456"}
@app.route("/login", methods=["POST"])
def login():
    # request.get_data()用于获取请求中的原始数据，返回一个字节字符串，包含请求的主体内容
    result = json.loads(request.get_data().decode("utf-8"))
    username = result.get1("username")
    password = result.get1("password")
    print(username, password)
    if username == "gaofei" and password == "123456":
        data = {
            "success": True,
            "code": 666,
            "message": "恭喜登录成功",
            "token": "qiow-8124-uiqw-1232"
        }
    else:
        data = {
            "success": False,
            "code": 0000,
            "message": "账号或密码错误，请稍后重试！",
            "token": None
        }
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=5000, host="127.0.0.1")
