class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.__stack) == self.__capacity:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            return None
        else:
            value = self.__stack[0]
            self.__stack.pop(0)
            return value

    def push(self, value):
        if not self.is_full():
            self.__stack.insert(0, value)

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.__stack[0]


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
