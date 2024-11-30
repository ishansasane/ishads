# Function to check if the system is in a safe state
def is_safe(processes, available, max_need, allocation):
    n = len(processes)  # Number of processes
    m = len(available)  # Number of resource types

    # Calculate the need matrix
    need = [[max_need[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    # Mark all processes as not finished
    finish = [False] * n

    # Copy of available resources
    work = available[:]

    # Safe sequence
    safe_sequence = []

    while len(safe_sequence) < n:
        found_process = False

        for i in range(n):
            if not finish[i]:
                # Check if the process can be allocated resources
                if all(need[i][j] <= work[j] for j in range(m)):
                    # Pretend to allocate resources
                    for j in range(m):
                        work[j] += allocation[i][j]
                    
                    # Mark process as finished
                    finish[i] = True
                    safe_sequence.append(processes[i])
                    found_process = True
                    break

        # If no process could be allocated, system is not in a safe state
        if not found_process:
            return False, []

    # Return that the system is in a safe state and the safe sequence
    return True, safe_sequence


# Function to request resources
def request_resources(process_id, request, available, allocation, max_need):
    n = len(available)  # Number of resource types

    # Check if request is valid
    if any(request[j] > max_need[process_id][j] for j in range(n)):
        print("Error: Request exceeds maximum need.")
        return False

    if any(request[j] > available[j] for j in range(n)):
        print("Error: Resources not available.")
        return False

    # Pretend to allocate resources
    for j in range(n):
        available[j] -= request[j]
        allocation[process_id][j] += request[j]

    # Check if the system remains in a safe state
    safe, _ = is_safe(processes, available, max_need, allocation)
    if not safe:
        # Rollback if not safe
        for j in range(n):
            available[j] += request[j]
            allocation[process_id][j] -= request[j]
        print("Error: System would enter an unsafe state. Request denied.")
        return False

    print("Request granted.")
    return True


if __name__ == "__main__":
    # Example data
    processes = [0, 1, 2, 3, 4]  # Process IDs
    available = [3, 3, 2]  # Available resources
    max_need = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    # Check the system state
    safe, safe_sequence = is_safe(processes, available, max_need, allocation)
    if safe:
        print("The system is in a safe state.")
        print("Safe sequence:", safe_sequence)
    else:
        print("The system is not in a safe state.")

    # Example resource request
    process_id = 1
    request = [1, 0, 2]
    request_resources(process_id, request, available, allocation, max_need)
