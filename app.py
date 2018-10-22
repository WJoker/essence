from flask import Flask
from configs.config import secret_key


app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
app.secret_key = secret_key


from routes.index import main as index_routes
app.register_blueprint(index_routes)


if __name__ == '__main__':
    """
    代码运行入口
    debug 模式可以自动加载代码的变动, 所以不用重启程序
    host 参数指定为 '0.0.0.0' 可以让别的机器访问
    """
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)