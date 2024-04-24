import time
import os

def task2():
    # get the pid of this process
    pid = os.getpid()
    for i in range(5):
        print(f"Task {pid} is running")
        time.sleep(1)

if __name__ == "__main__":
    task2()