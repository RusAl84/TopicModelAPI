from flask import Flask, request, jsonify
from flask_cors import CORS
from tmodel import tmodel

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():  # put application's code here
    return "Тематическое моделирование текстов"

@app.route('/tmodel', methods=['POST'])
def foo():
    data = request.json
    text = data['text']
    topic_num = data['topic_num']
    print(text)
    print(topic_num)
    tmodel(text, topic_num) 
    return jsonify("http://localhost:5000/static/vis.html"), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
app.run(host='0.0.0.0')