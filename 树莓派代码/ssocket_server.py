import datetime
import os
import socket
import time

import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)


def left():
    # gpio.output(12,False)
    # gpio.output(16,False)
    # gpio.output(22,False)
    gpio.output(18, True)


def right():
    gpio.output(12, True)
    # gpio.output(16,False)
    # gpio.output(22,False)
    # gpio.output(18,False)


def straight_high():
    gpio.output(12, True)
    gpio.output(18, True)


def real_straight():
    # forword 5s
    endTime = datetime.datetime.now() + datetime.timedelta(seconds=2)
    while True:
        straight_high()
        if datetime.datetime.now() >= endTime:
            break


def real_right():
    # right 2 s
    endTime = datetime.datetime.now() + datetime.timedelta(seconds=0.8)
    while True:
        right()
        if datetime.datetime.now() >= endTime:
            break


def real_left():
    # left 2 s
    endTime = datetime.datetime.now() + datetime.timedelta(seconds=0.8)
    while True:
        left()
        if datetime.datetime.now() >= endTime:
            break


def return_1():
    endTime = datetime.datetime.now() + datetime.timedelta(seconds=1.6)
    while True:
        left()
        if datetime.datetime.now() >= endTime:
            break


host = '192.168.12.1'
port = 8001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)
connection, address = sock.accept()
while True:
    try:
        connection.settimeout(10)
        buf = connection.recv(1024).decode()
        print(buf)
        if buf == '122':
            print("straight")
            os.system("aplay straight2s.wav")
            real_straight()
            time.sleep(2)
        if buf == '123':
            print("left")
            os.system("aplay left.wav")
            real_left()
            time.sleep(2)
        if buf == '124':
            print("right")
            os.system("aplay right.wav")
            real_right()
            time.sleep(2)
        if buf == '125':
            print("return")
            os.system("aplay return.wav")
            return_1()
            time.sleep(2)
    except socket.timeout:
        print("time out ")
    # connection.close()
