class Node:
    def __init__(self, val, next_ = None):
        self.val = val
        self.next = next_
    def __repr__(self):
        return "Node({}, {})".format(self.val, self.next)

class LinkedList:
    def __init__(self):
        self.head = None
        self.pointer = None
    def insert(self, ind, node):
        if ind == 0:
            if self.pointer is None:
                self.head = node
            else:
                node.next = self.head
                self.head = node
            self.pointer = self.head
        elif ind == 1:
            if self.pointer.next is None:
                self.pointer.next = node
            else:
                node.next = self.pointer.next
                self.pointer.next = node
            self.pointer = self.head
        else:
            self.pointer = self.pointer.next
            self.insert(ind - 1, node)
    def access(self, ind):
        if (ind == 0) and (self.pointer is not None):
            val = self.pointer.val
            self.pointer = self.head
            return val
        else:
            self.pointer = self.pointer.next
            return self.access(ind - 1)

    def remove(self, ind):
        if ind == 0:
            self.head = self.head.next
        elif ind == 1:
            tmp = self.pointer.next
            self.pointer.next = self.pointer.next.next
            tmp.next = None
            self.pointer = self.head
        else:
            self.pointer = self.pointer.next
            self.remove(ind - 1)

node_1 = Node('a')
node_2 = Node('b')
node_3 = Node('c')
node_4 = Node('d')

llist = LinkedList()
llist.insert(0, node_2)
llist.insert(1, node_3)
llist.insert(0, node_1)
print(llist.head)
llist.remove(1)
print(llist.head)
