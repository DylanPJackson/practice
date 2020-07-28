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
        if self.head is None:
            raise Exception("LinkedList empty, access failed")
        if (ind == 0) and (self.pointer is not None):
            val = self.pointer.val
            self.pointer = self.head
            return val
        else:
            self.pointer = self.pointer.next
            return self.access(ind - 1)

    def remove(self, ind):
        if self.head is None:
            raise Exception("LinkedList is empty, remove failed")            
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

"""
    Tests
        Access on empty - exception
        Remove on empty - Exception
        Insert out of bounds - Exception
        Access out of bounds - Exception
        Remove out of bounds - Exception
        Insert on empty - OK
        Insert at front - OK
        Insert at back - OK
        Insert somewhere in list - OK
        Remove front - OK
        Remove back - OK
        Remove somewhere in middle - OK
        Access front - OK
        Access back - OK
        Access somewhere in middle - OK
"""
def test_access_empty():
    llist = LinkedList()
    try:
        llist.access()
        return 0
    except Exception:
        return 1

def test_remove_empty():
    llist = LinkedList()
    try:
        llist.remove(1)
        return 0
    except:
        return 1        

def tests():
    if test_access_empty():
        print("Access on empty : Passed")
    else:
        print("Access on empty : Failed")
    if test_remove_empty():
        print("Remove on empty : Passed")
    else:
        print("Remove on empty : Failed")
        
def main():
    tests()

main()
