class Stack:

    def __init__(self, string: str):
        self.stack = string

    def isEmpty(self):
        return not bool(self.stack)

    def push(self, element: str):
        self.stack += element

    def pop(self):
        last_element = self.stack[-1]
        self.stack = self.stack[:-1]
        return last_element

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


