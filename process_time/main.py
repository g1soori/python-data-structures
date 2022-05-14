
def min_time(n, process_time, task_time):
    process_time.sort()
    task_time.reverse()
    process_num = 0
    execution_time = []

    for index, task in enumerate(task_time):
        exec_t = task + process_time[process_num]
        execution_time.append(exec_t)
        if index != 0 and index % 4 == 0:
            process_num += 1

    print(execution_time)



n = 2
processorTime = [8, 10]
taskTime = [2, 2, 3, 1, 8, 7, 4, 5]


min_time(n, processorTime, taskTime)