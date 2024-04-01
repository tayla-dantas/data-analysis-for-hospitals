class Stack:

    def __init__(self):
        self.list = []

    def push(self, el):
        return self.list.append(el)

    def pop(self):
        last_element = len(self.list) - 1
        return self.list.pop(last_element)

    def peek(self):
        last_element = len(self.list) - 1
        return self.list.index(last_element)

    def is_empty(self):
        return len(self.list) == 0
