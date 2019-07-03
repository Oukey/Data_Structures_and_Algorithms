class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return None

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):  # метод проверки на пустоту
        return self.stack == []

'''
st = 2. Stack()
print(st.is_empty())
st.push(1)
st.push('2')
st.push(3.14)
print(st.size())
print(st.is_empty())
print(st.peek())
while st.size() > 0:
    st.peek()
    st.pop()
    st.pop()
    print(st.size())
'''
