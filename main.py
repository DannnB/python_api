import os
import settings

from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def home(name=None):
    return render_template('home.html', name=name)

@app.route('/users', methods=['GET'])
def users():
    return jsonify({
        'users': [
            {
                'id': 'ajf924jgdfvn0e09',
                'username': 'dan'
            }
        ]
    })


if __name__ == '__main__':
    app.run(debug=True)
