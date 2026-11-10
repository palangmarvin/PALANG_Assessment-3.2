from collections import deque

from Array import letters

print("=== V. QUEUE IMPLEMENTATION (FIFO) ===")
queue = deque()

print("Enqueuing letters into the Queue:")
for letter in letters:
    queue.append(letter)  # ENQUEUE at rear
    print(f"ENQUEUE {letter} | Front -> {list(queue)} <- Rear")

print("\nDequeuing letters from the Queue:")
while len(queue) > 0:
    dequeued = queue.popleft()  # DEQUEUE from front
    print(f"DEQUEUE {dequeued} | Remaining Queue (Front -> Rear): {list(queue) if queue else 'Empty'}")

print("Queue is empty")