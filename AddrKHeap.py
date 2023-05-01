import array

class HeapElement(object):
    def __init__(self, key, element_id, index):
        self.key = key
        self.element_id = element_id
        self.index = index

    def set_index(self, new_index):
        self.index = new_index

    def get_index(self):
        return self.index

    def set_key(self, new_key):
        self.key = new_key

    def get_key(self):
        return self.key
    
    def get_element_id(self):
        return self.element_id
    
    def __eq__(self, other):
        # Allows you to overload the == operator
        return self.key == other.get_key()

    def __ne__(self, other):
        # Allows you to overload the != operator
        return self.key != other.get_key()

    def __lt__(self, other):
        # Allows you to overload the < operator
        return self.key < other.get_key()

    def __le__(self, other):
        # Allows you to overload the <= operator
        return self.key <= other.get_key()

    def __gt__(self, other):
        # Allows you to overload the > operator
        return self.key > other.get_key()

    def __ge__(self, other):
        # Allows you to overload the >= operator
        return self.key >= other.get_key()

    def __str__(self):
        return "HeapElement: Key: " + str(self.key) + " NodeId: " + str(self.element_id)


class AddrKHeap(object):
    def __init__(self, k = 4):
        assert k >= 2
        self.k = k
        self.heap = []
        self.size = 0
        self.element_index = {}
        
    def empty(self):
        return not self.size

    def get_size(self):
        return self.size

    def __parent(self, i):
        return (i - 1) // self.k

    def __child(self, i, j):
        return self.k * i + j

    def insert(self, key, element_id):
        self.heap.append(HeapElement(key, element_id, self.size))
        self.element_index[element_id] = self.size
        self.size += 1
        self.__sift_up(self.size - 1)

    def __update_index_of_element(self, index, new_index):
        e = self.heap[index]
        self.element_index[e.get_element_id()] = new_index;
        e.set_index(new_index)

    def __swap(self, i, j):
        self.__update_index_of_element(j, i)
        self.__update_index_of_element(i, j)
        self.heap[j], self.heap[i] = self.heap[i], self.heap[j]

    def __sift_up(self, i):
        while i > 0:
            parent = self.__parent(i)
            if self.heap[parent] > self.heap[i]:
                self.__swap(parent, i)
                i = parent
            else:
                break

    def front_key(self):
        if (self.empty()):
            return None
        return self.heap[0].get_key()

    def front_element_id(self):
        if (self.empty()):
            return None
        return self.heap[0].get_element_id()

    def extract_min(self):
        if self.size == 0:
            return None
        min_element = self.heap[0]
        del self.element_index[min_element.get_element_id()]
        last_element = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1
        if self.size > 0:
            self.heap[0] = last_element
            self.element_index[last_element.get_element_id()] = 0
            last_element.set_index(0)
            self.__sift_down(0)
        return min_element

    def deleteMinNode(self):
        return self.extract_min().get_element_id()

    def update(self, element_id, new_key):
        if (not self.contains(element_id)):
            self.insert(new_key, element_id)
        else:
            self.decreaseKey(element_id, new_key)

    def decreaseKey(self, element_id, new_key):
        if (not self.contains(element_id)):
            return

        index = self.element_index[element_id]
        assert index < len(self.heap), "index " + str(index) + " is out of bounds; trying to do stuff with node " + str(element_id)
        self.heap[index].set_key(new_key)
        self.__sift_up(index)

    def __sift_down(self, i):
        while self.__child(i, 1) < self.size:
            min_child = self.__min_child(i)
            if self.heap[i] > self.heap[min_child]:
                self.__swap(i, min_child)
                i = min_child
            else:
                break

    def __min_child(self, i):
        min_child = self.__child(i, 1)
        for j in range(2, self.k + 1):
            if self.__child(i, j) < self.size and self.heap[self.__child(i, j)] < self.heap[min_child]:
                min_child = self.__child(i, j)
        return min_child

    def contains(self, element_id):
        return (element_id in self.element_index)

    def remove(self, element_id):
        if (not self.contains(element_id) and not self.empty()):
            return

        self.decreaseKey(element_id, float("-inf"))
        self.extract_min()
        
    def is_heap(self):
        for i in range(1, self.size):
            parent = self.__parent(i)
            if self.heap[parent] > self.heap[i]:
                return False
        return True
        
    def __str__(self):
        return ", ".join([str(e) for e in self.heap])