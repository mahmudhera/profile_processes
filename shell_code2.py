import time
import os

def task2():
    # get the pid of this process
    pid = os.getpid()
    for i in range(5):
        val = 10
        for j in range(15):
            val = val * val

if __name__ == "__main__":
    task2()