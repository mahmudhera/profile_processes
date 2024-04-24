"""
monitor resource usages of proceses using psutil
"""

import psutil
import os
import time

def get_user_name():
    return psutil.users()[0].name

def get_list_of_processes():
    return psutil.process_iter()

def main(pid_to_monitor):
    # get user name
    user_name = get_user_name()

    # get start time of this process
    pid_this_proess = os.getpid()
    pid_this_proess = -1
    
    # get info of process to monitor
    process_to_monitor = psutil.Process(pid_to_monitor)
    create_time_of_process_to_monitor = process_to_monitor.create_time()

    print('Monitoring process with PID:', pid_to_monitor)
    print('Process name:', process_to_monitor.name())
    print('Process create time:', create_time_of_process_to_monitor)

    processes = get_list_of_processes()
    for process in processes:
        # print pid and creation time and user
        print(f"PID: {process.pid} - Name: {process.name()} - User: {process.username()} - Create time: {process.create_time()}")

    # stats to record
    peak_memory = 0.0
    total_cpu_time = 0.0

    last_time_monitored = time.time()

    while process_to_monitor.is_running():
        time.sleep(1)
        # get list of processes    
        processes = get_list_of_processes()

        processes_to_benchmark = []
        for process in processes:
            if process.create_time() >= create_time_of_process_to_monitor and process.username() == user_name:
                processes_to_benchmark.append(process)

        current_recorded_memory = 0.0
        current_recorded_cpu_percentage = 0.0
        for process in processes_to_benchmark:
            current_recorded_memory += process.memory_info().rss
            current_recorded_cpu_percentage += process.cpu_percent()

        delta_time = time.time() - last_time_monitored
        peak_memory = max(peak_memory, current_recorded_memory)
        total_cpu_time += current_recorded_cpu_percentage * delta_time / 100.0

        #print(process_to_monitor, delta_time, current_recorded_cpu_percentage, total_cpu_time)
        # show how many processes are being monitored
        print(f"Monitoring {len(processes_to_benchmark)} processes")

        last_time_monitored = time.time()

    print(f"Peak memory usage: {peak_memory}")
    print(f"Total CPU time: {total_cpu_time}")


if __name__ == "__main__":
    # the first command line argument is the pid of the process to monitor
    # e.g. python main.py 1234
    # if no pid is provided, the script will exit
    if len(os.sys.argv) < 2:
        os.sys.exit(1)
    pid_to_monitor = int(os.sys.argv[1])
    main(pid_to_monitor)