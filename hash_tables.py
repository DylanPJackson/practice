from linked_lists import LinkedList
from linked_lists import Node

class HashTable:
    def __init__(self, size):
        self.size = int(1.3 * size)
        self.table = [LinkedList() for i in range(self.size)]

    def __repr__(self):
        r_str = ""
        for i in range(self.size):
            if i == self.size - 1:
                r_str = r_str + repr(self.table[i].head)
            else:
                r_str = r_str + repr(self.table[i].head) + "\n" 
        return r_str

    def hash(self, key):
        return (((len(key) * 3) + 8) * ord(key[0])) % self.size

    def access(self, key):
        ind = self.hash(key)
        try:
            val = self.table[ind].access_by_key(key)
            return val
        except:
            raise Exception("access failed, {} not in table".format(key))

    def insert(self, key, val):
        ind = self.hash(key)
        node = Node(val = (key,val))
        self.table[ind].insert_at_end(node)

    def delete(self, key):
        ind = self.hash(key)
        try:
            self.table[ind].remove_by_key(key)
        except:
            raise Exception("delete failed, {} not in table".format(key))

def main():
    p_1 = ("Dylan", "Human")
    p_2 = ("Lauren", "Egg")
    p_3 = ("Colin", "Monkey")
    h_table = HashTable(3)
    h_table.insert(p_1[0], p_1[1])
    print(h_table)
    h_table.insert(p_2[0], p_2[1])
    print(h_table)
    h_table.insert(p_3[0], p_3[1])
    print(h_table)
    h_table.delete(p_1[0])
    print(h_table)
    h_table.insert(p_1[0], p_1[1])
    h_table.delete(p_2[0])
    print(h_table)

    
main()
