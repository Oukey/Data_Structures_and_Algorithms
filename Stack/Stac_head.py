class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop(-1)
        else:
            return None

    def push(self, value):
        if len(self.stack) == 0:
            return self.stack.append(value)
        else:
            return self.stack.insert(0, value)

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):  # метод проверки на пустоту
        return self.stack == []
