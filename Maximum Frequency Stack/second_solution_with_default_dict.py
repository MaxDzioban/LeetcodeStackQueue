from collections import defaultdict
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def top_value(self):
        return self.top.value if self.top else None

    def is_empty(self):
        return self.top is None

class FreqStack:
    def __init__(self):
        self.stack = Stack()
        self.freqs = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        freq = self.freqs[val]
        self.max_freq = max(self.max_freq, freq)
        self.stack.push((val, freq))

    def pop(self) -> int:
        if not self.max_freq:
            return None
        
        val_to_pop = None
        temp_stack = Stack()
        while not self.stack.is_empty():
            val, freq = self.stack.pop()
            if freq == self.max_freq:
                val_to_pop = val
                break
            temp_stack.push((val, freq))

        while not temp_stack.is_empty():
            val, freq = temp_stack.pop()
            self.stack.push((val, freq))
        
        if val_to_pop is None:
            return None
        
        self.freqs[val_to_pop] -= 1
        if self.freqs[val_to_pop] == 0:
            del self.freqs[val_to_pop]
        self.max_freq = max(self.freqs.values()) if self.freqs else 0
        
        return val_to_pop
