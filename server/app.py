from flask import Flask, render_template, jsonify, request
from hatesonar import Sonar

sonar = Sonar()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/analyze', methods=['POST'])
def analyzer():
    j = request.get_json()
    text = j.get('text')
    res = sonar.ping(text=text)

    return jsonify(res)


if __name__ == '__main__':
    app.run()
