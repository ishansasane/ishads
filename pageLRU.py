# Function to implement LRU page replacement algorithm
def lru_page_replacement(pages, capacity):
    memory = []  # List to store the pages in memory
    page_faults = 0  # Count of page faults

    # Dictionary to track the most recent use of each page
    recent_usage = {}

    for i, page in enumerate(pages):
        # If the page is not in memory, it's a page fault
        if page not in memory:
            # If memory is full, we need to replace the least recently used page
            if len(memory) == capacity:
                # Find the least recently used page
                lru_page = min(recent_usage, key=recent_usage.get)
                memory.remove(lru_page)  # Remove the LRU page from memory
                del recent_usage[lru_page]  # Remove it from usage tracking

            # Add the new page to memory
            memory.append(page)
            page_faults += 1  # Increment the page fault count

        # Update the most recent usage of the current page
        recent_usage[page] = i

    # Output the final content of memory and the number of page faults
    print(f"\nPages in memory: {memory}")
    print(f"Total page faults: {page_faults}")


# Example usage
if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]  # Page reference string
    capacity = 3  # Capacity of the page frame (memory size)

    lru_page_replacement(pages, capacity)
