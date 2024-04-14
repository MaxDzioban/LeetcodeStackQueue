class Node:
    """class Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """class Queue"""
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def __len__(self):
        return self.size

    # def __str__(self): unused
    #     return str(self.size)

class MyStack:
    """class MyStack"""
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def empty(self):
        return len(self.queue1) == 0

    def push(self, item):
        #у порожню чергу
        if self.queue1.is_empty():
            self.queue1.add(item)
        else:
            #з 1 в 2
            while not self.queue1.is_empty():
                self.queue2.add(self.queue1.pop())
            #у 1
            self.queue1.add(item)
            #2 назад у 1
            while not self.queue2.is_empty():
                self.queue1.add(self.queue2.pop())

    def pop(self):
        if self.empty():
            raise IndexError("Stack is empty")
        return self.queue1.pop()

    def top(self):
        if self.empty():
            raise IndexError("Stack is empty")
        return self.queue1.peek()

myStack = MyStack()
myStack.push(1)
myStack.push(2)
print("Top element:", myStack.top())
# Виведе: 2
print("Popped element:", myStack.pop())
# Виведе: 2
