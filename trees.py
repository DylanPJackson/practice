class Node:
    def __init__(self, val):
        self.val = val
        self.count = 1

    def __repr__(self):
        return "Node({})".format(self.val)

class Tree:
    def __init__(self, left = None, root = None, right = None):
        self.root = root
        self.left = left
        self.right = right

    def __repr__(self):
        return "Tree({}, {}, {})".format(self.left, self.root, self.right) 

    def binary_search(self, val):
        """
        Assumes ordered as binary search tree
        """
        if self.root == None:
            raise Exception("Value has not been found")
        elif self.root.val == val:
            return self.root.val
        elif self.root.val > val:
            if self.has_right():
                return(self.right.binary_search(val))
            else:
                raise Exception("Value has not been found")
        else:
            if self.has_left():
                return(self.left.binary_search(val))
            else:
                raise Exception("Value has not been found")


    def has_left(self):
        if self.left is None:
            return False
        else:
            return True

    def has_right(self):
        if self.right is None:
            return False
        else:
            return True

    def has_children(self):
        if self.has_right() or self.has_left():
            return True
        else:
            return False

    def search(self, val):
        if self.root is None:
            return False
        elif self.root.val == val:
            return True
        elif val < self.root.val:
            if self.has_left():
                return self.left.search(val)
            else:
                return False
        else:
            if self.has_right():
                return self.right.search(val)
            else:
                return False

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        elif self.root.val == val:
            self.root.count += 1
        elif val < self.root.val:
            if self.has_left():
                self.left.insert(val)
            else:
                self.left = Tree(root = Node(val)) 
        else:
            if self.has_right():
                self.right.insert(val)
            else:
                self.right = Tree(root = Node(val))

    def delete(self, val):
        if self.root is None:
            return
        else:
            if self.root.val == val:
                if self.root.count > 1:
                    self.root.count -= 1
                else:
                    if not(self.has_children()):
                        self.root = None
                    elif not(self.has_right()) and self.has_left():
                        self.root = self.left
                    elif self.has_right() and not(self.has_left()):
                        self.root = self.right
                    else:
                        l_max = self.left.in_order_max()
                        self.delete(l_max)
                        self.root.val = l_max
            elif val < self.root.val:
                self.left.delete(val)
            else:
                self.right.delete(val)

    def in_order_max(self):
        if not(self.has_children()):
            return self.root.val
        elif not(self.has_right()):
            return self.root.val
        else:
            return self.right.in_order_max()

def main():
    val_1 = 1
    val_2 = 2
    val_3 = 3
    tree = Tree()
    tree.insert(val_1)
    tree.insert(val_2)
    print(tree)
    print(tree.binary_search(val_1))
    print(tree.binary_search(val_3))


main()
