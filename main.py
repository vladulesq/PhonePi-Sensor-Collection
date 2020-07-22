#!python3
import webbrowser
import threading
from flask_sockets import Sockets
from flask import Flask,render_template, Response
import json
from time import time
import time
from datetime import datetime
app = Flask(__name__)

sockets = Sockets(app)

dataX=""
dataY=""
dataZ=""
#py main.py


@sockets.route('/accelerometer') 
def echo_socket(ws):
    f=open("accelerometer.txt","w")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message, file=f)
    f.close()


@sockets.route('/gyroscope')
def echo_socket(ws):
    f=open("gyroscope.txt","w")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message,file=f)
    f.close()

@sockets.route('/magnetometer')
def echo_socket(ws):
    f=open("magnetometer.txt","w")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message,file=f)
    f.close()

@sockets.route('/orientation')
def echo_socket(ws):
    f=open("orientation.txt","w")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message,file=f)
    f.close()

@sockets.route('/stepcounter')
def echo_socket(ws):
    f=open("stepcounter.txt","w")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message,file=f)
    f.close()

@sockets.route('/thermometer')
def echo_socket(ws):
    f=open("thermometer.txt","w")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message,file=f)
    f.close()

@sockets.route('/lightsensor')
def echo_socket(ws):
    f=open("lightsensor.txt","w")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message,file=f)
    f.close()

@sockets.route('/proximity')
def echo_socket(ws):
    f=open("proximity.txt","w")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message,file=f)
    f.close()

@sockets.route('/geolocation')
def echo_socket(ws):
    f=open("geolocation.txt","w")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message,file=f)
    f.close()

@app.route('/') 
def hello(): 
    return 'Hello World!'

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('192.168.1.110', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()




