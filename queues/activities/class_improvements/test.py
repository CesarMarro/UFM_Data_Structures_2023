from LinearQueue import LinearQueue


# Queue instance
queue = LinearQueue(5)
print(queue)

# Enqueues
queue.enqueue('A')
print(queue)
queue.enqueue('B')
print(queue)
queue.enqueue('C')
print(queue)
queue.enqueue('D')
print(queue)
queue.enqueue('E')
print(queue)
queue.enqueue('F') # Queue Overflow
queue.enqueue('G') # Queue Overflow

# Dequeues
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
print("Peeking: %s" % (queue.peek()))
print("Search for letter E: "+ str(queue.search("E")))
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
print("Peeking: %s" % (queue.peek()))
print("Search for letter F: "+ str(queue.search("F")))
queue.dequeue()
print(queue)
queue.dequeue() # Queue Underflow (2nd scenario)
queue.dequeue() # Queue Underflow (2nd scenario)

