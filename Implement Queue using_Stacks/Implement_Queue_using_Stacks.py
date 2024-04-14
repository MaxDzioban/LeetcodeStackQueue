class Node:
    """class Node"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    """class Stack"""
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        popped_item = self.top.data
        self.top = self.top.next
        return popped_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data

    def __len__(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count

class MyQueue:
    """
    MyQueue
    """
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, item):
        self.stack1.push(item)

    def pop(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def size(self):
        return len(self.stack1) + len(self.stack2)
