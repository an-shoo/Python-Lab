class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        return self.queue

# Testing Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.display())
print("Popped item:", stack.pop())
print("Stack after popping:", stack.display())

# Testing Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", queue.display())
print("Dequeued item:", queue.dequeue())
print("Queue after dequeuing:", queue.display())
