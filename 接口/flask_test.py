from flask import Flask  # 使用Python语言快速实现一个网站或Web服务

app = Flask(__name__)


@app.route('/')  # 装饰器 通过变量来调用该函数
def index():
    return 'hello world!'


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run()