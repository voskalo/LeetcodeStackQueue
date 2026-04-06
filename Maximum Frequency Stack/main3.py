'''Maximu Frequency Stack'''

class Node:
    '''node class'''

    def __init__(self, val):
        '''init'''

        self.value = val
        self.next = None



class Stack:
    '''stack class'''

    def __init__(self):
        '''init'''

        self.top_node = None

    def push(self, x: int):
        '''push funct'''

        new = Node(x)
        new.next = self.top_node
        self.top_node = new

    def is_empty(self):
        '''chech if empty'''
        return self.top_node is None


    def pop(self):
        '''pop funct'''

        if not self.top_node:
            return None

        val = self.top_node.value
        self.top_node = self.top_node.next

        return val






class FreqStack:
    '''FreqStack class'''

    def __init__(self):
        ...

    def push(self, val: int) -> None:
        ...

    def pop(self) -> int:
        ...


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
