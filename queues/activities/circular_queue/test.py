from CircularQueue import CircularQueue


# Queue instance
queue = CircularQueue(5)
print(queue)


queue.circular_enqueue('A')
print(queue)
queue.circular_enqueue('B')
print(queue)
queue.circular_enqueue('C')
print(queue)
queue.circular_dequeue()
print(queue)
queue.circular_enqueue('D')
print(queue)
queue.circular_dequeue()
print(queue)

print("Search for letter F: "+ str(queue.circular_search("F")))
queue.circular_enqueue('E')
print(queue)
queue.circular_enqueue('F') 
print(queue)
queue.circular_enqueue('G') 
print(queue)
print("Search for letter F: "+ str(queue.circular_search("F")))
queue.circular_enqueue('A')# Queue Overflow


queue.circular_dequeue()
print(queue)
queue.circular_dequeue()
print(queue)
queue.circular_dequeue()
print(queue)
print("Search for letter G: "+ str(queue.circular_search("G")))
queue.circular_dequeue()
print(queue)
queue.circular_dequeue()
print(queue)
queue.circular_dequeue()# Queue Underflow



