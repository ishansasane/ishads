def find_avg_time_rr(processes, burst_time, time_quantum):
    n = len(processes)

    # Initialize remaining burst times and waiting times
    remaining_bt = burst_time[:]  # Copy of burst times
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Initialize variables
    time = 0  # Current time

    # Process queue in Round Robin fashion
    while True:
        done = True  # Check if all processes are done

        for i in range(n):
            if remaining_bt[i] > 0:
                done = False  # At least one process is not done

                if remaining_bt[i] > time_quantum:
                    # Process runs for a time quantum
                    time += time_quantum
                    remaining_bt[i] -= time_quantum
                else:
                    # Process finishes execution
                    time += remaining_bt[i]
                    waiting_time[i] = time - burst_time[i]
                    remaining_bt[i] = 0

        if done:  # Break the loop if all processes are done
            break

    # Calculate turnaround times
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    # Calculate average waiting time and turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Print results
    print("Process ID    Burst Time    Waiting Time    Turnaround Time")
    for i in range(n):
        print(f"{processes[i]}            {burst_time[i]}            {waiting_time[i]}            {turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")


# Example usage
if __name__ == "__main__":
    processes = [1, 2, 3]  # Process IDs
    burst_time = [10, 5, 8]  # Burst times for each process
    time_quantum = 2  # Time quantum for Round Robin

    find_avg_time_rr(processes, burst_time, time_quantum)
