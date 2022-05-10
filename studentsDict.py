# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:31:40 2022

@author: 21pt37
"""
students = {
    
    '18PT01' :{'name':'name1','class':'18PT'},
    '18PT02' :{'name':'name2','class':'18PT'}       
}

from flask import Flask
app=Flask(__name__)
@app.route("/students/<id>")
def get_students(id):
    return students[id]
    
if __name__ == "__main__":
    app.run();
    
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
"""