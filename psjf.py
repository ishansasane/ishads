def find_waiting_time(processes, n, bt, wt):
    # Sort processes by burst time
    sorted_indices = sorted(range(n), key=lambda x: bt[x])
    sorted_bt = [bt[i] for i in sorted_indices]

    # Rearrange processes as per sorted burst time
    sorted_processes = [processes[i] for i in sorted_indices]

    wt[0] = 0  # Waiting time for the first process is always 0

    # Calculate waiting time for each process
    for i in range(1, n):
        wt[i] = sorted_bt[i - 1] + wt[i - 1]

    return sorted_processes, sorted_indices


def find_turnaround_time(n, sorted_bt, wt, tat):
    # Calculate turnaround time by adding burst time and waiting time
    for i in range(n):
        tat[i] = sorted_bt[i] + wt[i]


def find_avg_time(processes, n, bt):
    wt = [0] * n
    tat = [0] * n

    # Calculate waiting time and get sorted process order
    sorted_processes, sorted_indices = find_waiting_time(processes, n, bt, wt)

    # Reorder burst time to match sorted order
    sorted_bt = [bt[i] for i in sorted_indices]

    # Calculate turnaround time
    find_turnaround_time(n, sorted_bt, wt, tat)

    # Map back waiting time and turnaround time to original process order
    original_wt = [0] * n
    original_tat = [0] * n

    for i, idx in enumerate(sorted_indices):
        original_wt[idx] = wt[i]
        original_tat[idx] = tat[i]

    # Calculate total waiting time and turnaround time
    total_wt = sum(original_wt)
    total_tat = sum(original_tat)

    # Calculate average waiting time and average turnaround time
    avg_wt = total_wt / n
    avg_tat = total_tat / n

    print("Process ID    Burst Time    Waiting Time    Turnaround Time")
    for i in range(n):
        print(f"{processes[i]}            {bt[i]}            {original_wt[i]}            {original_tat[i]}")

    print("\nAverage Waiting Time:", avg_wt)
    print("Average Turnaround Time:", avg_tat)


# Example usage
if __name__ == "__main__":
    processes = [1, 2, 3]  # Process IDs
    burst_time = [5, 9, 6]  # Burst times for each process
    n = len(processes)

    find_avg_time(processes, n, burst_time)
