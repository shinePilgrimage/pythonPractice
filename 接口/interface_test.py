from flask import Flask
import json

server = Flask(__name__)
print(server.config)


# 定义url请求路径
@server.route('/')
def hello():
    return 'hello world!'


@server.route('/index', methods=['get', 'post'])  # 第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get
def index():
    res1 = {'msg': '第一个接口', 'msg_code': 1}
    return json.dumps(res1, ensure_ascii=False)


@server.route('/test/api', methods=['post'])
def test():
    res2 = {"msg": "第二个接口", "msg_code": 2}
    return json.dumps(res2, ensure_ascii=False)


if __name__ == '__main__':
    server.run(host='172.28.151.235', debug=True, port=5000)
