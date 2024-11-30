# Function to implement FIFO page replacement algorithm
def fifo_page_replacement(pages, capacity):
    # Initialize an empty list for the frames (pages in memory)
    memory = []
    page_faults = 0  # To count the number of page faults

    # Loop through each page in the page reference string
    for page in pages:
        # If the page is not already in memory, we have a page fault
        if page not in memory:
            # If memory is full, remove the oldest page (first one in FIFO)
            if len(memory) == capacity:
                memory.pop(0)  # Remove the first page in the list (FIFO order)
            # Add the new page to memory
            memory.append(page)
            page_faults += 1  # Increase the page fault count
        # If the page is already in memory, no page fault occurs
        else:
            print(f"Page {page} is already in memory.")

    # Output the final content of memory and the number of page faults
    print(f"\nPages in memory: {memory}")
    print(f"Total page faults: {page_faults}")


# Example usage
if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]  # Page reference string
    capacity = 3  # Capacity of the page frame (memory size)

    fifo_page_replacement(pages, capacity)
