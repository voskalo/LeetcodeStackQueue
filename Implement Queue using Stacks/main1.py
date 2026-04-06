'''Implement Queue using Stacks'''


class Node:
    '''node class'''

    def __init__(self, val):
        '''node init'''

        self.value = val
        self.next = None


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
        self.in_stack = Stack()
        self.out_stack = Stack()


    def push(self, x: int) -> None:
        '''push funct'''
        self.in_stack.push(x)


    def rotate(self):
        '''rotate funcct'''

        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())


    def pop(self) -> int:
        '''pop funct'''
        self.rotate()
        return self.out_stack.pop()


    def peek(self) -> int:
        '''peek funct'''

        self.rotate()
        return self.out_stack.peek()


    def empty(self) -> bool:
        return self.in_stack.is_empty() and self.out_stack.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
