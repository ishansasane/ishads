# Function to implement SCAN Disk Scheduling
def scan_disk_scheduling(requests, head, disk_size, direction):
    total_seek_time = 0  # Total head movement
    seek_sequence = []  # To store the order of served requests

    print(f"Initial head position: {head}")
    print(f"Direction: {direction}")

    # Split requests into left and right of the head
    left = [req for req in requests if req < head]
    right = [req for req in requests if req >= head]

    # Sort both sides
    left.sort()
    right.sort()

    if direction == "left":
        # Serve the left requests first, then the right requests
        seek_sequence.extend(reversed(left))
        seek_sequence.extend(right)
    elif direction == "right":
        # Serve the right requests first, then the left requests
        seek_sequence.extend(right)
        seek_sequence.extend(reversed(left))

    # Calculate total seek time
    current_position = head
    for req in seek_sequence:
        total_seek_time += abs(req - current_position)
        current_position = req

    print("Seek sequence:", " -> ".join(map(str, seek_sequence)))
    print(f"Total seek time: {total_seek_time}")
    print(f"Average seek time: {total_seek_time / len(seek_sequence):.2f}")


# Example usage
if __name__ == "__main__":
    # List of I/O requests
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head_position = 53  # Initial position of the disk head
    disk_size = 200  # Size of the disk (0 to disk_size-1)
    initial_direction = "left"  # Initial direction of head movement

    scan_disk_scheduling(requests, head_position, disk_size, initial_direction)
