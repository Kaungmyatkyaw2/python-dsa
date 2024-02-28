class StackOverflowException(Exception):
    def __init__(self, message):
        super().__init__(message)


class StackUnderflowException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Stack:
    def __init__(self, __size):
        self.__items = []
        self.__top = -1
        self.__size = __size

    def isFull(self):
        return self.__size - 1 == self.__top

    def isEmpty(self):
        return self.__top == -1

    def push(self, val):
        if not self.isFull():
            self.__top += 1
            self.__items = self.__items[0 : self.__top] + [val]
        else:
            raise StackOverflowException("Stack is full.")

    def pop(self):
        if not self.isEmpty():
            tempTop = self.__top
            self.__top -= 1
            return self.__items[tempTop]
        else:
            raise StackUnderflowException("Stack is empty.")

    def peek(self):
        return self.__items[self.__top]

    def getSize(self):
        return self.__top + 1
