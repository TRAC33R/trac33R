class Stack:
    def __init__(self, elements=[]):
        self.stack = elements
       
    
    def peek(self):
        return self.stack[-1]

    def push(self, element):
        self.stack.append(element)
        return None

    def pop(self):
        temp = self.stack[-1]
        del self.stack[-1]
        return temp

    def __repr__(self):
        return str(self.stack)