'''Implement Queue using Stacks'''


class Node:
    '''node class'''

    def __init__(self, val):
        '''node init'''

        self.value = val
        self.naet = None


class Stack:
    '''stack class'''

    def __init__(self):
        '''init'''
        self.top = None
        self._size = 0


    def push(self, x: int):
        '''push funct'''
        new = Node(x)
        new.next = self.top
        self.top = new
        self._size += 1

    def is_empty(self):
        '''validation if is empty'''

        return self.top is None

    def pop(self):
        '''pop funct'''

        if self.is_empty():
            return None

        val = self.top.value
        self.top = self.top.next
        self._size -= 1

        return val


    def peek(self):
        '''peek funct'''

        if self.top:
            return self.top.value
        else:
            return None

    def size(self):
        '''size funct'''
        return self._size




class MyQueue:
    '''class docstr'''

    def __init__(self):
        '''init'''
        ...

    def push(self, x: int) -> None:
        ...

    def pop(self) -> int:
        ...

    def peek(self) -> int:
        ...

    def empty(self) -> bool:
        ...


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
