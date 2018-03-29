CS333: Homework 1 - Scheduler
========

![Trains](trains.jpg)

From Professor Herb Mayer's CS333 Course. [PSU Course Description](https://www.pdx.edu/computer-science/cs333)

Scheduler
-------
General Rules: Implement all Homework (HW) in C or C++. Submit all sources, including .c, .cpp, and .h files, if any. Also hand-in sample inputs and generated outputs. Write the date, your name, school, class, year, and the name of this HW clearly on each separately compiled module in the form of a program comment. Your written discussion of your outputs is an important part of HW1.

>**Abstract**: Design, implement, document, test, and debug the schedulers of three types of Operating Systems. Do not be scared! Only the (simulation of the) timing analysis of each scheduler is of interest, thus design and implementation efforts are quite small. The simulator measures key performance data, such as throughput, wait time, and turn-around time.
>
>One OS is a strict batch system with a non-preemptive First Come First Serve (FCFS) scheduler. The second OS uses a non-preemptive, high-priority first (HPF) scheduler, while the third OS uses a preemptive round robin (RR) scheduler with a variable time-quantum with varying context switch overhead. Design meaningful input data, run them through all schedulers, generate output data, and interpret and discuss the results. To start, use the sample data from this HW assignment. In addition, provide 3 additional, meaningful input scenarios, all more complex than the samples in this HW.

#### Detail:
Homework 1 consists of 5 parts with equal weight:
1. Design and implement a scheduler for a non-preemptive FCFS batch system,

1. Ditto for non-preemptive HPF batch system, and

1. Ditto for preemptive RR scheduler; you’ll vary time quantum and overhead.

1. Invent meaningful input data and run them through your schedulers to produce output

1. Discuss the generated data. Hand in your discussion in typed form, not long-hand

#### Input:
Input to the schedulers is a *list of processes*, for which you know the execution time in milliseconds and other key parameters. We do not answer the delicate question, how you know the execution time! For your program input, each process is represented by a triple of decimal numbers `(id, time, priority)`. These multiple processes are scheduled and compete for the CPU resource.

Note: Parentheses are given in the actual input. They are solely used here for logical grouping. `id` is the name of (the number of) the process; `time` is the time in milliseconds that process `id` needs to run to completion, and `priority` is the priority of process `id`. A plausible input sample for two processes with the names 1 and 4 is:

```
1   2   3
4   50  6
```

The meaning of these triples is as follows:
`1 2 3 // process p1 uses 2 milliseconds to run, has priority`
`4 50 6 // process p4 uses 50 milliseconds, has priority 6. 0 is highest`

Use the definitions below to compute for each process *Throughput*, *Wait Time*, and *Turn-around Time*. Compute these for each process handled by each of the 3 schedulers, and average for all processes.

#### Definitions:

* **Throughput**: Number of jobs (processes) completed per time unit

* **Waiting Time**: The total time a process is in Ready Queue

* **Average Waiting Time**: Average Waiting Time of n processes is their total waiting time by n

* **Turn-around Time**: span of time of submission to completion time

For the preemptive RR scheduler, vary the time quantum `q` from 1 to 5 milliseconds (ms). Also, for each `q` selected, vary the overhead `o` of a context switch from `0 ms` up to `q` itself. There is no need to vary the `o` beyond `q`. When a process scheduled by the RR system has received all time needed to completion, do not add a final `o` unit in the computation of the total time for that process. Also the first time around, act as if the initial schedule overhead `o` is `0`.

---------------
### Sample Execution:
Use the sample outputs below as a guide for the degree of detail you should generate for this HW.

#### Example 1:

```
Enter triples: process id, time in ms, and priority:
For example:
1 12 0
3 9 1
2 99 9
process 1 needs 12 ms and has priority 0, very high,
process 3 needs 9 ms and has priority 1.
and so on ...

1 2 3
2 1 2

Process list in FCFS order as entered:
1 2 3
2 1 2
End of list.

fcfs wait of p1 = 0
fcfs wait of p2 = 2
average wait for 2 procs = 1
fcfs turn-around time for p1 = 2
fcfs turn-around time for p2 = 3
average turn-around for 2 procs = 2.5
fcfs throughput for 2 procs = 0.666667 proc/ms
<><> end FCFS <><>

Process list in HPF order:
2 1 2
1 2 3
End of list.

hpf wait of p2 = 0
hpf wait of p1 = 1
average wait time for 2 procs = 0.5
hpf turn-around for p2 = 1
hpf turn-around for p1 = 3
average turn-around for 2 procs = 2
hpf throughput for 2 procs = 0.666667 proc/ms
<><> end HPF schedule <><>

Process list for RR in order entered:
1 2 3
2 1 2
End of list.

preemptive RR schedule, quantum = 1 overhead = 0
RR TA time for finished p2 = 2, needed: 1 ms, and: 1 time slices.
RR TA time for finished p1 = 3, needed: 2 ms, and: 2 time slices.
RR Throughput, 2 p, with q: 1, o: 0, is: 0.666667 p/ms, or 666.667 p/us
Average RR TA, 2 p, with q: 1, o: 0, is: 2.5

preemptive RR schedule, quantum = 1 overhead = 1
RR TA time for finished p2 = 3, needed: 1 ms, and: 1 time slices.
RR TA time for finished p1 = 5, needed: 2 ms, and: 2 time slices.
RR Throughput, 2 p, with q: 1, o: 1, is: 0.4 p/ms, or 400 p/us
Average RR TA, 2 p, with q: 1, o: 1, is: 4

preemptive RR schedule, quantum = 2 overhead = 0
RR TA time for finished p1 = 2, needed: 2 ms, and: 1 time slices.
RR TA time for finished p2 = 3, needed: 1 ms, and: 1 time slices.
RR Throughput, 2 p, with q: 2, o: 0, is: 0.666667 p/ms, or 666.667 p/us
Average RR TA, 2 p, with q: 2, o: 0, is: 2.5

preemptive RR schedule, quantum = 2 overhead = 1
RR TA time for finished p1 = 2, needed: 2 ms, and: 1 time slices.
RR TA time for finished p2 = 4, needed: 1 ms, and: 1 time slices.
RR Throughput, 2 p, with q: 2, o: 1, is: 0.5 p/ms, or 500 p/us
Average RR TA, 2 p, with q: 2, o: 1, is: 3

preemptive RR schedule, quantum = 2 overhead = 2
RR TA time for finished p1 = 2, needed: 2 ms, and: 1 time slices.
RR TA time for finished p2 = 5, needed: 1 ms, and: 1 time slices.
RR Throughput, 2 p, with q: 2, o: 2, is: 0.4 p/ms, or 400 p/us
Average RR TA, 2 p, with q: 2, o: 2, is: 3.5
<> end preemptive RR schedule <>
```

#### Example 2:
```
Enter triples: process id, time in ms, and priority:
For example:
1 12 0
3 9 1
2 99 9
process 1 needs 12 ms and has priority 0, very high,
process 3 needs 9 ms and has priority 1.
and so on ...

1 10 5
2 8 1
3 12 7

Process list in FCFS order as entered:
1 10 5
2 8 1
3 12 7
End of list.

fcfs wait of p1 = 0
fcfs wait of p2 = 10
fcfs wait of p3 = 18
average wait for 3 procs = 9.33333
fcfs turn-around time for p1 = 10
fcfs turn-around time for p2 = 18
fcfs turn-around time for p3 = 30
average turn-around for 3 procs = 19.3333
fcfs throughput for 3 procs = 0.1 proc/ms
<><> end FCFS <><>

Process list in HPF order:
2 8 1
1 10 5
3 12 7
End of list.

hpf wait of p2 = 0
hpf wait of p1 = 8
hpf wait of p3 = 18
average wait time for 3 procs = 8.66667
hpf turn-around for p2 = 8
hpf turn-around for p1 = 18
hpf turn-around for p3 = 30
average turn-around for 3 procs = 18.6667
hpf throughput for 3 procs = 0.1 proc/ms
<><> end HPF schedule <><>

Process list for RR in order entered:
1 10 5
2 8 1
3 12 7
End of list.

preemptive RR schedule, quantum = 1 overhead = 0
RR TA time for finished p2 = 23, needed: 8 ms, and: 8 time slices.
RR TA time for finished p1 = 27, needed: 10 ms, and: 10 time slices.
RR TA time for finished p3 = 30, needed: 12 ms, and: 12 time slices.
RR Throughput, 3 p, with q: 1, o: 0, is: 0.1 p/ms, or 100 p/us
Average RR TA, 3 p, with q: 1, o: 0, is: 26.6667

preemptive RR schedule, quantum = 1 overhead = 1
RR TA time for finished p2 = 45, needed: 8 ms, and: 8 time slices.
RR TA time for finished p1 = 53, needed: 10 ms, and: 10 time slices.
RR TA time for finished p3 = 59, needed: 12 ms, and: 12 time slices.
RR Throughput, 3 p, with q: 1, o: 1, is: 0.0508475 p/ms, or 50.8475 p/us
Average RR TA, 3 p, with q: 1, o: 1, is: 52.3333

preemptive RR schedule, quantum = 2 overhead = 0
RR TA time for finished p2 = 22, needed: 8 ms, and: 4 time slices.
RR TA time for finished p1 = 26, needed: 10 ms, and: 5 time slices.
RR TA time for finished p3 = 30, needed: 12 ms, and: 6 time slices.
RR Throughput, 3 p, with q: 2, o: 0, is: 0.1 p/ms, or 100 p/us
Average RR TA, 3 p, with q: 2, o: 0, is: 26

preemptive RR schedule, quantum = 2 overhead = 1
RR TA time for finished p2 = 32, needed: 8 ms, and: 4 time slices.
RR TA time for finished p1 = 38, needed: 10 ms, and: 5 time slices.
RR TA time for finished p3 = 44, needed: 12 ms, and: 6 time slices.
RR Throughput, 3 p, with q: 2, o: 1, is: 0.0681818 p/ms, or 68.1818 p/us
Average RR TA, 3 p, with q: 2, o: 1, is: 38

preemptive RR schedule, quantum = 2 overhead = 2
RR TA time for finished p2 = 42, needed: 8 ms, and: 4 time slices.
RR TA time for finished p1 = 50, needed: 10 ms, and: 5 time slices.
RR TA time for finished p3 = 58, needed: 12 ms, and: 6 time slices.
RR Throughput, 3 p, with q: 2, o: 2, is: 0.0517241 p/ms, or 51.7241 p/us
Average RR TA, 3 p, with q: 2, o: 2, is: 50

preemptive RR schedule, quantum = 3 overhead = 0
RR TA time for finished p2 = 23, needed: 8 ms, and: 3 time slices.
RR TA time for finished p1 = 27, needed: 10 ms, and: 4 time slices.
RR TA time for finished p3 = 30, needed: 12 ms, and: 4 time slices.
RR Throughput, 3 p, with q: 3, o: 0, is: 0.1 p/ms, or 100 p/us
Average RR TA, 3 p, with q: 3, o: 0, is: 26.6667

preemptive RR schedule, quantum = 3 overhead = 1
RR TA time for finished p2 = 30, needed: 8 ms, and: 3 time slices.
RR TA time for finished p1 = 36, needed: 10 ms, and: 4 time slices.
RR TA time for finished p3 = 40, needed: 12 ms, and: 4 time slices.
RR Throughput, 3 p, with q: 3, o: 1, is: 0.075 p/ms, or 75 p/us
Average RR TA, 3 p, with q: 3, o: 1, is: 35.3333

preemptive RR schedule, quantum = 3 overhead = 2
RR TA time for finished p2 = 37, needed: 8 ms, and: 3 time slices.
RR TA time for finished p1 = 45, needed: 10 ms, and: 4 time slices.
RR TA time for finished p3 = 50, needed: 12 ms, and: 4 time slices.
RR Throughput, 3 p, with q: 3, o: 2, is: 0.06 p/ms, or 60 p/us
Average RR TA, 3 p, with q: 3, o: 2, is: 44

preemptive RR schedule, quantum = 3 overhead = 3
RR TA time for finished p2 = 44, needed: 8 ms, and: 3 time slices.
RR TA time for finished p1 = 54, needed: 10 ms, and: 4 time slices.
RR TA time for finished p3 = 60, needed: 12 ms, and: 4 time slices.
RR Throughput, 3 p, with q: 3, o: 3, is: 0.05 p/ms, or 50 p/us
Average RR TA, 3 p, with q: 3, o: 3, is: 52.6667

preemptive RR schedule, quantum = 4 overhead = 0
RR TA time for finished p2 = 20, needed: 8 ms, and: 2 time slices.
RR TA time for finished p1 = 26, needed: 10 ms, and: 3 time slices.
RR TA time for finished p3 = 30, needed: 12 ms, and: 3 time slices.
RR Throughput, 3 p, with q: 4, o: 0, is: 0.1 p/ms, or 100 p/us
Average RR TA, 3 p, with q: 4, o: 0, is: 25.3333

preemptive RR schedule, quantum = 4 overhead = 1
RR TA time for finished p2 = 24, needed: 8 ms, and: 2 time slices.
RR TA time for finished p1 = 32, needed: 10 ms, and: 3 time slices.
RR TA time for finished p3 = 37, needed: 12 ms, and: 3 time slices.
RR Throughput, 3 p, with q: 4, o: 1, is: 0.0810811 p/ms, or 81.0811 p/us
Average RR TA, 3 p, with q: 4, o: 1, is: 31

preemptive RR schedule, quantum = 4 overhead = 2
RR TA time for finished p2 = 28, needed: 8 ms, and: 2 time slices.
RR TA time for finished p1 = 38, needed: 10 ms, and: 3 time slices.
RR TA time for finished p3 = 44, needed: 12 ms, and: 3 time slices.
RR Throughput, 3 p, with q: 4, o: 2, is: 0.0681818 p/ms, or 68.1818 p/us
Average RR TA, 3 p, with q: 4, o: 2, is: 36.6667

preemptive RR schedule, quantum = 4 overhead = 3
RR TA time for finished p2 = 32, needed: 8 ms, and: 2 time slices.
RR TA time for finished p1 = 44, needed: 10 ms, and: 3 time slices.
RR TA time for finished p3 = 51, needed: 12 ms, and: 3 time slices.
RR Throughput, 3 p, with q: 4, o: 3, is: 0.0588235 p/ms, or 58.8235 p/us
Average RR TA, 3 p, with q: 4, o: 3, is: 42.3333

preemptive RR schedule, quantum = 4 overhead = 4
RR TA time for finished p2 = 36, needed: 8 ms, and: 2 time slices.
RR TA time for finished p1 = 50, needed: 10 ms, and: 3 time slices.
RR TA time for finished p3 = 58, needed: 12 ms, and: 3 time slices.
RR Throughput, 3 p, with q: 4, o: 4, is: 0.0517241 p/ms, or 51.7241 p/us
Average RR TA, 3 p, with q: 4, o: 4, is: 48

preemptive RR schedule, quantum = 5 overhead = 0
RR TA time for finished p1 = 20, needed: 10 ms, and: 2 time slices.
RR TA time for finished p2 = 23, needed: 8 ms, and: 2 time slices.
RR TA time for finished p3 = 30, needed: 12 ms, and: 3 time slices.
RR Throughput, 3 p, with q: 5, o: 0, is: 0.1 p/ms, or 100 p/us
Average RR TA, 3 p, with q: 5, o: 0, is: 24.3333

preemptive RR schedule, quantum = 5 overhead = 1
RR TA time for finished p1 = 23, needed: 10 ms, and: 2 time slices.
RR TA time for finished p2 = 27, needed: 8 ms, and: 2 time slices.
RR TA time for finished p3 = 36, needed: 12 ms, and: 3 time slices.
RR Throughput, 3 p, with q: 5, o: 1, is: 0.0833333 p/ms, or 83.3333 p/us
Average RR TA, 3 p, with q: 5, o: 1, is: 28.6667

preemptive RR schedule, quantum = 5 overhead = 2
RR TA time for finished p1 = 26, needed: 10 ms, and: 2 time slices.
RR TA time for finished p2 = 31, needed: 8 ms, and: 2 time slices.
RR TA time for finished p3 = 42, needed: 12 ms, and: 3 time slices.
RR Throughput, 3 p, with q: 5, o: 2, is: 0.0714286 p/ms, or 71.4286 p/us
Average RR TA, 3 p, with q: 5, o: 2, is: 33

preemptive RR schedule, quantum = 5 overhead = 3
RR TA time for finished p1 = 29, needed: 10 ms, and: 2 time slices.
RR TA time for finished p2 = 35, needed: 8 ms, and: 2 time slices.
RR TA time for finished p3 = 48, needed: 12 ms, and: 3 time slices.
RR Throughput, 3 p, with q: 5, o: 3, is: 0.0625 p/ms, or 62.5 p/us
Average RR TA, 3 p, with q: 5, o: 3, is: 37.3333

preemptive RR schedule, quantum = 5 overhead = 4
RR TA time for finished p1 = 32, needed: 10 ms, and: 2 time slices.
RR TA time for finished p2 = 39, needed: 8 ms, and: 2 time slices.
RR TA time for finished p3 = 54, needed: 12 ms, and: 3 time slices.
RR Throughput, 3 p, with q: 5, o: 4, is: 0.0555556 p/ms, or 55.5556 p/us
Average RR TA, 3 p, with q: 5, o: 4, is: 41.6667

preemptive RR schedule, quantum = 5 overhead = 5
RR TA time for finished p1 = 35, needed: 10 ms, and: 2 time slices.
RR TA time for finished p2 = 43, needed: 8 ms, and: 2 time slices.
RR TA time for finished p3 = 60, needed: 12 ms, and: 3 time slices.
RR Throughput, 3 p, with q: 5, o: 5, is: 0.05 p/ms, or 50 p/us
Average RR TA, 3 p, with q: 5, o: 5, is: 46

<><>end preemptive RR schedule <><>
```
