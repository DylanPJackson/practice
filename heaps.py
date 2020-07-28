class Heap:
    def __init__(self, type_ = 0):
        self.arr = []
        self.type = type_

    def __repr__(self):
        return str(self.arr) 

    @property
    def length(self):
        return len(self.arr)

    def peek(self):
        if self.arr == []:
            raise Exception("Heap empty, peek failed")
        else:
            return self.arr[0]

    # Gets parent index of given position
    def get_par(self, pos):
        if pos % 2 == 0:
            return int((pos - 2) / 2)
        else:
            return int((pos - 1) / 2)

    # Get child given index and specified left or right
    def get_child(self, ind, inc):
        new_ind = (ind * 2) + inc
        if new_ind == self.length:
            return (None, inc)
        else:
            return (self.arr[new_ind], inc)

    def insert(self, val, pos = None):
        """
            The pos = None is a cheeky trick I learned to get around 'self'
            being out of scope as an argument, which made it impossible to do
            pos = self.length
        """
        if pos is None:
            pos = self.length
        if pos == 0 and not(self.length == 0):
            return
        elif pos == 0:
            self.arr = [val]
        else:
            par = self.get_par(pos) 
            if ((self.type == 0 and val <= self.arr[par]) or 
               (self.type == 1 and val >= self.arr[par])):
                if pos == self.length:
                    self.arr.append(val)
            else:
                temp = self.arr[par]
                self.arr[par] = val
                if pos == self.length:
                    self.arr.append(temp)
                    self.insert(val, par)
                else:
                    self.arr[pos] = temp
                    self.insert(val, par)

    def delete(self):
        if self.length == 0:
            raise Exception("Heap empty, delete failed")
        elif self.length == 1:
            self.arr.pop(0)
        else:
            self.arr[0] = self.arr[self.length - 1]
            self.arr.pop(self.length - 1)
            ind = 0
            while(1):
                c1 = self.get_child(ind, 1)
                c2 = self.get_child(ind, 2)
                if c1[0] is None and c2[0] is None:
                    return
                elif c2[0] is None:
                    if ((self.type == 0 and c1[0] <= self.arr[ind]) or
                        (self.type == 1 and c1[0] >= self.arr[ind])):
                        return
                    else:
                        self.arr[(2*ind) + 1] = self.arr[ind]
                        self.arr[ind] = c1[0]
                        return
                else:
                    n_val = 0
                    if ((self.type == 0 and c1[0] < c2[0]) or
                        (self.type == 1 and c1[0] > c2[0])):
                        n_val = c2
                    else:
                        n_val = c1
                    if ((self.type == 0 and n_val[0] > self.arr[ind]) or
                        (self.type == 1 and n_val[0] < self.arr[ind])):
                        new_ind = (2 * ind) + n_val[1]
                        self.arr[new_ind] = self.arr[ind]
                        self.arr[ind] = n_val[0]
                        ind = new_ind
                    else:
                        return

def main():
    heap = Heap()
    print(heap)
    val_1 = 10
    val_2 = 7 
    val_3 = 8
    val_4 = 5
    val_5 = 6
    val_6 = 4
    heap.insert(val_2)
    print(heap)
    heap.insert(val_3)
    print(heap)
    heap.insert(val_4)
    print(heap)
    heap.delete()
    print(heap)
    heap.insert(val_3)
    print(heap)
    heap.insert(val_6)
    print(heap)
    heap.insert(val_1)
    print(heap)

main()
