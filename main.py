import os
import settings

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    return 'Returning some data...'


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
