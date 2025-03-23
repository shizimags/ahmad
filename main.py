# flask app

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/audio')
def audio():
    return render_template('audio.html')

if __name__ == '__main__':
    app.run(debug=True)