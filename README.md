# profile_processes
In this repo, we have an example of following:

1. How to use monitor.py (see shell_code.py)

# Requirements
```
psutil
```

## What shell_code.py does

This piece of code does the following:

1. it takes as a command line argument the PID of a process that it needs to monitor
1. as long as the process with the given pid (lets say this is Process P) is alive, this process will keep monitoring
1. in addition to monitoring P, our monitor will also track the processes that are owned by a user, and those spawned after P
1. when P finishes, our monitor exits by reporting CPU time and peak memory usage
1. the interval used by our monitor is 0.1 seconds

If we need to change the interval or the username, we need to do so in hard code.