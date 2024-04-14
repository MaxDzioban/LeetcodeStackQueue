class Node:
    """class Node"""
    def __init__(self,item,next=None):
        self.item=item
        self.next=next

        self.frequency=1

class FreqStack:
    """class FreqStack"""
    def __init__(self):
        self.head=None
        self.max_frequency=0

    def push(self,item):
        self.head=Node(item,self.head)
        curr=self.head.next
        while curr is not None:
            if curr.item == self.head.item:
                self.head.frequency+=curr.frequency
                break
            curr=curr.next
        if self.head.frequency > self.max_frequency:
            self.max_frequency = self.head.frequency

    def pop(self):
        if self.head is None:
            return None
        
        curr=self.head
        value=0
        
        if curr.frequency==self.max_frequency:
            value=curr.item
            self.head=curr.next
        else:
            while curr.next is not None:
                if curr.next.frequency == self.max_frequency:
                    value=curr.next.item
                    curr.next=curr.next.next
                    break
                curr=curr.next
        
        self.max_frequency-=1
        curr=self.head
        while curr is not None:
            if curr.frequency>self.max_frequency:
                self.max_frequency+=1
                break
            curr=curr.next
        return value