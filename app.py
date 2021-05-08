from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/api/tm')
def tm():


    return 'Pink Floyd!'

if __name__ == '__main__':
    app.run()
