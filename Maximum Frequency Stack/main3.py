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
        '''init'''

        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        '''oush funct'''

        freq = self.freq.get(val, 0) + 1
        self.freq[val] = freq

        if freq > self.max_freq:
            self.max_freq = freq

        if freq not in self.group:
            self.group[freq] = Stack()

        self.group[freq].push(val)

    def pop(self) -> int:
        '''pop funct'''
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1

        if self.group[self.max_freq].is_empty():
            self.max_freq -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
