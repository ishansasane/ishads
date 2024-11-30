import threading
import time
from queue import Queue

# Buffer size
BUFFER_SIZE = 5

# Shared queue
queue = Queue(BUFFER_SIZE)


def producer(queue):
    for i in range(1, 11):  # Produces 10 items
        item = f"Item {i}"
        time.sleep(1)  # Simulating production time
        queue.put(item)
        print(f"Producer produced: {item}")


def consumer(queue):
    while True:
        item = queue.get()  # Get an item from the queue
        if item is None:  # Stop if sentinel value is received
            break
        time.sleep(2)  # Simulating consumption time
        print(f"Consumer consumed: {item}")
        queue.task_done()  # Mark task as done


if __name__ == "__main__":
    # Create producer and consumer threads
    producer_thread = threading.Thread(target=producer, args=(queue,))
    consumer_thread = threading.Thread(target=consumer, args=(queue,))

    # Start the threads
    producer_thread.start()
    consumer_thread.start()

    # Wait for the producer to finish
    producer_thread.join()

    # Send sentinel value to stop the consumer
    queue.put(None)

    # Wait for the consumer to finish
    consumer_thread.join()

    print("Producer-Consumer simulation completed.")
