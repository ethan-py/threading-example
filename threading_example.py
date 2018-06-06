#IMPORT THREADING - PART OF PYTHON, NO NEED TO USE PIP
import threading
from threading import Thread

#DEFINE FIRST VARIABLE TO SPAM THE WORD "HI"
def hi():
    while True:
        print("hi\n")

#DEFINE SECOND VARIABLE TO SPAM THE WORD "HELLO"
def hello():
    while True:
        print("hello\n")

#DEFINE THIRD VARIABLE TO SPAM THE WORD "HOLA"
def hola():
    while True:
        print("hola\n")

#CREATE EMPTY LIST OF THREADS
threads = []

#SET UP THREADING ON THE HI FUNCTION AND ADD TO LIT
hithread = threading.Thread(target=hi, args=())
hithread.start()
threads.append(hithread)

#SET UP THREADING ON THE HELLO FUNCTION AND ADD TO LIT
hellothread = threading.Thread(target=hello, args=())
hellothread.start()
threads.append(hellothread)

#SET UP THREADING ON THE HOLA FUNCTION AND ADD TO LIT
holathread = threading.Thread(target=hola, args=())
holathread.start()
threads.append(holathread)

#JOIN THE THREADS
for thread in threads:
    thread.join()

#THIS WILL HAVE ALL 3 WORDS BE SPAMMED CONTINUOUSLY AT ONCE, SUPER USEFUL FOR MONITORS AND MORE <3
