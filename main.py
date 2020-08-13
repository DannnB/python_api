import os
import settings

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/contacts')
def contact():
    return render_template('pages/contact.html')

@app.route('/terms-and-conditions')
def tandcs():
    return render_template('pages/tandcs.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template('pages/login.html')

@app.route('/users/<usr>')
def user(usr):
    return render_template('pages/profile.html',zebra=usr)


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
