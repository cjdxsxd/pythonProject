from flask import Flask

app = Flask(__name__)
# 配置
app.config['DEBUG'] = True
app.config.update(
    DEBUG=True
)

@app.route('/')
def hello_world():
    return ' Hello World! Hello liJianGuo!'


@app.route("/shangxudong")
def hell_shangxudong():
    return "Hello,shangxudong!"


@app.route("/lijianguo")
def hell_lijianguo():
    return "Hello,LiJianGuo!"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
