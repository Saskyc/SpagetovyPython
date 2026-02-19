from datetime import datetime
from time import sleep
from threading import Thread

def toprint():
    sleep(1)
    print("1", datetime.now())
    
def tofr():
    print("2", datetime.now())

for i in range(1000000000):
    t1 = Thread(target=toprint)
    t2 = Thread(target=tofr)

    t2.start()
    t1.start()
    
    t2.join()
    t1.join()
    sleep(1)
