#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'
    
@app.route('/hello')
def hello():
    return 'Hello'
    
@app.route('/user/list')
def user_list():
    return 'user list page'
    
@app.route('/use/<int:id>')
def demo_get(id):
    return 'user id=%d' %id
    
if __name__ == '__main__':
    app.run()
