from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/api/tmodel', methods=['POST'])
def getTModel():
    text = request.get_data(as_text="true")
    # mas = ""
    print(text)
    return text


if __name__ == '__main__':
    app.run()
