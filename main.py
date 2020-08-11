import os
import settings

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
#hi

@app.route('/')
@app.route('/<name>')
def home(name=None):
    return render_template('home.html', name=name)

@app.route('/users', methods=['GET'])
def users():
    searchId = request.args.get('id', '')
    print(searchId)
    # TODO: add search of database to find user
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
