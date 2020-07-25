class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "Node({}, {})".format(self.val, self.next)

class Queue:
    def __init__(self, val = None):
        if val is None:
            self.head = None
            self.tail = None
        else:
            first = Node(val)
            self.head = first
            self.tail = first

    def __repr__(self):
        return "Queue({})".format(self.head)

    def front(self):
        if self.head is None:
            raise Exception("Queue empty, front failed")
        else:
            return self.head.val

    def back(self):
        if self.tail is None:
            raise Exception("Queue empty, back failed")
        else:
            return self.tail.val

    def dequeue(self):
        try:
            val = self.head.val
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return val
        except:
            raise Exception("Queue empty, dequeue failed")

    def enqueue(self, val):
        if self.tail is None:
            self.tail = Node(val)
            self.head = self.tail
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
            
def main():
    queue = Queue()
    val_1 = 1
    val_2 = 2
    val_3 = 3
    queue.enqueue(val_1)
    queue.enqueue(val_2)
    queue.dequeue()
    print(queue)

main()
