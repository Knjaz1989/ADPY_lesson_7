class Stack:

    def __init__(self, string: str):
        self.stack = string
        if self.__get_balance(self.stack):
            print("Сбалансированно")
        else:
            print("Несбалансированно")

    def __get_balance(self, string):
        new_string = ''
        for item in string:
            if string[0] == '}' or string[0] == ')' or string[0] == ']':
                return False
            elif item == '{' or item == '(' or item == '[':
                new_string += item
            elif new_string[-1] + item == '{}' or new_string[-1] + item == '()' or new_string[-1] + item == '[]':
                new_string = new_string[:-1]
        if new_string:
            return False
        else:
            return True

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

s = Stack('[[{())}]')
print(s.isEmpty(), s.push(']'), s.pop(), s.peek(), s.size())

