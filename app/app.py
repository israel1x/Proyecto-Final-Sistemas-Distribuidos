#!/usr/bin/env python
# coding: utf-8

# Dependencies:
# pip install flask
# pip install redis

from flask import Flask
from flask import request
import flask
import redis
import time
import json
import os

app = Flask(__name__)
app.debug = True


@app.route('/status')
def status():
    return 'RUNNING'

@app.route('/news/<dateNews>')
def getNewsRedis(dateNews):
	#r = redis.StrictRedis(host='localhost',port='6379', db=0)
	#news = r.get(dateNews)
    return 'Las Noticias ' + dateNews


if __name__ == "__main__":
    app.run()