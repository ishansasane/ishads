# FCFS Scheduling Algorithm
def find_waiting_time(processes, n, bt, wt):
    wt[0] = 0  # Waiting time for the first process is always 0

    # Calculate waiting time for each process
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]


def find_turnaround_time(processes, n, bt, wt, tat):
    # Calculate turnaround time by adding burst time and waiting time
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def find_avg_time(processes, n, bt):
    wt = [0] * n
    tat = [0] * n

    # Calculate waiting time and turnaround time
    find_waiting_time(processes, n, bt, wt)
    find_turnaround_time(processes, n, bt, wt, tat)

    # Calculate total waiting time and turnaround time
    total_wt = sum(wt)
    total_tat = sum(tat)

    # Calculate average waiting time and average turnaround time
    avg_wt = total_wt / n
    avg_tat = total_tat / n

    print("Process ID    Burst Time    Waiting Time    Turnaround Time")
    for i in range(n):
        print(f"{processes[i]}            {bt[i]}            {wt[i]}            {tat[i]}")

    print("\nAverage Waiting Time:", avg_wt)
    print("Average Turnaround Time:", avg_tat)


# Example usage
if __name__ == "__main__":
    processes = [1, 2, 3]  # Process IDs
    burst_time = [5, 9, 6]  # Burst times for each process
    n = len(processes)

    find_avg_time(processes, n, burst_time)
