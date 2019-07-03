import Stack
import re


def postfix(example):
    t_list = re.split('([^0-9])', example)
    stack = Stack.Stack()
    for t in t_list:
        if t == '' or t == ' ':
            continue
        elif t == '+':
            sum = stack.pop() + stack.pop()
            stack.puch(sum)
        elif t == '*':
            result = stack.pop() * stack.pop()
            stack.push(result)
        elif t == '/':
            result = stack.pop() / stack.pop()
            stack.push(result)
        else:
            stack.push(int(t))
    return stack.pop()
