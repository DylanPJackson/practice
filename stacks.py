class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return "Node({}, {})".format(self.val, self.next)

class Stack:
    def __init__(self, top = None):
        self.top = top

    def __repr__(self):
        return "Stack({})".format(self.top)

    def peek(self):
        if self.top is None:
            raise Exception("Stack is empty, peek failed")
        else:
            return self.top.val

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty, pop failed")
        else:
            val = self.top.val
            self.top = self.top.next
            return val

    def push(self, val):
        new_top = Node(val, self.top)
        self.top = new_top

def main():
    val_1 = 1
    val_2 = 2
    val_3 = 3
    stack = Stack()
    stack.push(val_2)
    stack.push(val_1)
    stack.push(val_3)
    print(stack.pop())
    print(stack)

main()
