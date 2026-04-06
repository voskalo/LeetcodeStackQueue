'''Implement Stack using Queues'''


class Node:
    '''node class'''

    def __init__(self, val):
        '''init'''

        self.value = val
        self.next = None


class Queue:
    '''queue class'''

    def __init__(self):
        '''init'''

        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        '''validation if is empty'''
        return self._size == 0


    def push(self, x: int):
        '''push funct'''

        new = Node(x)

        if self.is_empty():
            self.head = self.tail = new

        else:
            self.tail.next = new
            self.tail = new

        self._size += 1


    def pop(self):
        '''pop funct'''

        if self.is_empty():
            return None

        val = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1

        return val


    def peek(self):
        '''peek funct'''

        if self.head:
            return self.head.value

        return None



    def size(self):
        '''size funct'''
        return self._size

class MyStack:

    def __init__(self):
        ...

    def push(self, x: int) -> None:
        ...

    def pop(self) -> int:
        ...

    def top(self) -> int:
        ...

    def empty(self) -> bool:
        ...


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
