"""
This is a do-nothing shell.
This script simply runs a loop to print a few lines.
Before doing anything, this script will start monitor.py.
Lets see what monitor.py does.
"""


import os
import time
import multiprocessing

def task(pid):
    # spawn five more processes that execute task2
    #for i in range(3):
    #    cmd = "python shell_code2.py&"
    #    os.system(cmd)
    
    for i in range(5):
        print(f"Mother: Task {pid} is running")
        val = 10
        for j in range(22):
            val = val * val
        time.sleep(0.1)

if __name__ == "__main__":
    # get the pid of this process
    pid = os.getpid()

    # show pid
    print(f"PID: {pid}")

    # start the monitor script
    os.system(f"python monitor.py {pid}&")

    task(pid)