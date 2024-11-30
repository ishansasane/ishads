# Function to implement FCFS Disk Scheduling
def fcfs_disk_scheduling(requests, head):
    total_seek_time = 0  # Total head movement
    current_position = head  # Starting head position

    print(f"Initial head position: {head}")
    print("Seek sequence:", end=" ")

    for request in requests:
        # Calculate the distance between the current head position and the next request
        seek_distance = abs(request - current_position)
        total_seek_time += seek_distance  # Add to total seek time
        current_position = request  # Move the head to the current request

        print(request, end=" ")

    print(f"\nTotal seek time: {total_seek_time}")
    print(f"Average seek time: {total_seek_time / len(requests):.2f}")


# Example usage
if __name__ == "__main__":
    # List of I/O requests
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head_position = 53  # Initial position of the disk head

    fcfs_disk_scheduling(requests, head_position)
