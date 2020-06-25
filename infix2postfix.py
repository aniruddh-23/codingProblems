# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:24:20 2020

@author: TheKa
"""


class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        if(len(self.stack)==0):
            return True
        return False
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if self.isEmpty():
            return False
        value = self.stack[-1]
        self.stack = self.stack[:-1]
        return value
    def peek(self):
        if self.isEmpty():
            return False
        return self.stack[-1]

def infix2post(infix):
    priority = {"^":3,"*":2,"/":2,"+":1,"-":1,"(":0}
    postfix = ""
    stack = Stack()
    for i in infix:
        if i == ")" :
            popped = stack.pop()
            print(1)
            while popped != "(":
                postfix += popped
                popped = stack.pop()
        elif i =="(" :
            print(2)
            stack.push(i)
        elif i in priority.keys():
            print(3)
            while (not stack.isEmpty()) and priority[stack.peek()] >= priority[i]:
                postfix += stack.pop()
            stack.push(i)
        else :
            print(4)
            postfix += i
    while not stack.isEmpty():
        postfix += stack.pop()
    return postfix
infix = list("(A+B^D)/(E-F)+G")
print(infix2post(infix))
        