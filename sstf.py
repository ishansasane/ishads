# Function to implement SSTF Disk Scheduling
def sstf_disk_scheduling(requests, head):
    total_seek_time = 0  # Total head movement
    current_position = head  # Starting head position
    requests = requests[:]  # Copy of the requests list to manipulate
    seek_sequence = []  # To store the order of served requests

    print(f"Initial head position: {head}")

    while requests:
        # Find the request with the shortest seek time from the current position
        shortest_seek = min(requests, key=lambda r: abs(r - current_position))
        seek_distance = abs(shortest_seek - current_position)
        
        # Update seek time and move the head
        total_seek_time += seek_distance
        current_position = shortest_seek

        # Append the request to the seek sequence and remove it from the queue
        seek_sequence.append(shortest_seek)
        requests.remove(shortest_seek)

    print("Seek sequence:", " -> ".join(map(str, seek_sequence)))
    print(f"Total seek time: {total_seek_time}")
    print(f"Average seek time: {total_seek_time / len(seek_sequence):.2f}")


# Example usage
if __name__ == "__main__":
    # List of I/O requests
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head_position = 53  # Initial position of the disk head

    sstf_disk_scheduling(requests, head_position)
