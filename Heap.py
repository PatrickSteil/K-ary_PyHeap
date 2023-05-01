import array

class KHeap(object):
    def __init__(self, k = 4):
        assert k >= 2
        self.k = k
        self.heap = array.array('l')
        self.size = 0
        
    def empty(self):
        return not self.size

    def get_size(self):
        return self.size

    def __parent(self, i):
        return (i - 1) // self.k

    def __child(self, i, j):
        return self.k * i + j

    def insert(self, key):
        self.heap.append(key)
        self.size += 1
        self.__sift_up(self.size - 1)

    def insert_many(self, values):
        self.heap.extend(values)
        self.size += len(values)
        
        for i in range(self.size - len(values), self.size):
            self.__sift_up(i)

    def __sift_up(self, i):
        while i > 0:
            parent = self.__parent(i)
            if self.heap[parent] > self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break

    def extract_min(self):
        if self.size == 0:
            return None
        min_element = self.heap[0]
        last_element = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1
        if self.size > 0:
            self.heap[0] = last_element
            self.__sift_down(0)
        return min_element

    def __sift_down(self, i):
        while self.__child(i, 1) < self.size:
            min_child = self.__min_child(i)
            if self.heap[i] > self.heap[min_child]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
                i = min_child
            else:
                break

    def __min_child(self, i):
        min_child = self.__child(i, 1)
        for j in range(2, self.k + 1):
            if self.__child(i, j) < self.size and self.heap[self.__child(i, j)] < self.heap[min_child]:
                min_child = self.__child(i, j)
        return min_child
        
    def is_heap(self):
        for i in range(1, self.size):
            parent = self.__parent(i)
            if self.heap[parent] > self.heap[i]:
                return False
        return True
        
    def __str__(self):
        return str(self.heap)