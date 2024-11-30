# Function to implement C-SCAN Disk Scheduling
def c_scan_disk_scheduling(requests, head, disk_size):
    total_seek_time = 0  # Total head movement
    seek_sequence = []  # To store the order of served requests

    print(f"Initial head position: {head}")

    # Split requests into left and right of the head
    left = [req for req in requests if req < head]
    right = [req for req in requests if req >= head]

    # Sort both sides
    left.sort()
    right.sort()

    # C-SCAN: Serve the right requests, then jump to the leftmost and serve those
    seek_sequence.extend(right)
    seek_sequence.extend(left)

    # Calculate total seek time
    current_position = head
    for req in seek_sequence:
        total_seek_time += abs(req - current_position)
        current_position = req

    # Account for the jump from the last request to the first
    if left:
        total_seek_time += abs(disk_size - 1 - right[-1])  # From last right to the end
        total_seek_time += abs(disk_size - 1 - left[0])  # From end to first left

    print("Seek sequence:", " -> ".join(map(str, seek_sequence)))
    print(f"Total seek time: {total_seek_time}")
    print(f"Average seek time: {total_seek_time / len(seek_sequence):.2f}")


# Example usage
if __name__ == "__main__":
    # List of I/O requests
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head_position = 53  # Initial position of the disk head
    disk_size = 200  # Size of the disk (0 to disk_size-1)

    c_scan_disk_scheduling(requests, head_position, disk_size)
