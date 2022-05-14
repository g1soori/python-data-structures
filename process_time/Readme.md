The computing cluster has multiple processors, each with 4 cores. The number of tasks to handle is equal to the total number of cores in the cluster. Each task has a predicted execution time and each processor has a specified time when its core becomes available. Assuming that exactly 4 tasks are assigned to each processor and those tasks run independently(asynchronously) on the cores of the chosen processor, what is the earliest time that all tasks can be processed.

Example

n = 2

processorTime = [8, 10]

taskTime = [2, 2, 3, 1, 8, 7, 4, 5]

One optimal solution is as follows:

Assign the tasks with the execution times 2, 3, 7, and 8 to processor 0 that start at time 8.

Assign the tasks with the execution times 4, 2, 5, and 1 to processor 1 that start at time 10.

The first processor's cores finish at times (8+2), (8+3), (8+7), and (8+8), which are 10, 11, 15, and 16 respectively.

The second processor's cores finish at times (10+4), (10+2), (10+5), and (10+1), which are 14, 12, 15, and 11 respectively.

The maximum among those finishing times is 16. This is the earliest possible finish time.