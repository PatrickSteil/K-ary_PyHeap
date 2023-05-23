"""
Copyright 2023 Patrick Steil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

class HeapElement(object):
    def __init__(self, key, element_id, index):
        self.key = key                  # the key value of this element
        self.element_id = element_id    # an identifier for this element
        self.index = index              # the index of this element in the heap

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
        # Returns a string representation of this element
        return "HeapElement: Key: " + str(self.key) + " NodeId: " + str(self.element_id)


class AddrKHeap(object):
    def __init__(self, k = 4):
        assert k >= 2
        self.k = k                      # the k value for this k-ary heap
        self.heap = []                  # the underlying list to store elements
        self.size = 0                   # the number of elements in the heap
        self.element_index = {}         # a dictionary to keep track of element indexes
        
    def empty(self):
        # Returns True if the heap is empty
        return not self.size

    def get_size(self):
        # Returns the number of elements in the heap
        return self.size

    def __parent(self, i):
        # Returns the index of the parent element for the given index
        return (i - 1) // self.k

    def __child(self, i, j):
        # Returns the index of the j-th child of the element at index i
        return self.k * i + j

    def insert(self, element_id, key):
        # Inserts a new element with the given element_id and key value
        self.heap.append(HeapElement(key, element_id, self.size))
        self.element_index[element_id] = self.size
        self.size += 1
        self.__sift_up(self.size - 1)

    def __update_index_of_element(self, index, new_index):
        # Updates the index of the element at the given index
        e = self.heap[index]
        self.element_index[e.get_element_id()] = new_index;
        e.set_index(new_index)

    def __swap(self, i, j):
        # Swaps the positions of the elements at the given indexes
        self.__update_index_of_element(j, i)
        self.__update_index_of_element(i, j)
        self.heap[j], self.heap[i] = self.heap[i], self.heap[j]

    def __sift_up(self, i):
        # Restores the heap property
        while i > 0:
            parent = self.__parent(i)
            if self.heap[parent] > self.heap[i]:
                self.__swap(parent, i)
                i = parent
            else:
                break

    def front_key(self):
        # Returns the key of the smallest element in the heap
        if (self.empty()):
            return None
        return self.heap[0].get_key()

    def front_element_id(self):
        # Returns the element if of the smallest element in the heap
        if (self.empty()):
            return None
        return self.heap[0].get_element_id()

    def extract_min(self):
        # Returns the smallest element and deletes it from the queue
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
        # Returns the element id of the smallest element and deletes the element from the queue
        return self.extract_min().get_element_id()

    def update(self, element_id, new_key):
        # Calls decreaseKey of inserts the element with the new_key
        if (not self.contains(element_id)):
            self.insert(element_id, new_key)
        else:
            self.decreaseKey(element_id, new_key)

    def decreaseKey(self, element_id, new_key):
        # Updates the key of element_id
        if (not self.contains(element_id)):
            return

        index = self.element_index[element_id]
        assert index < len(self.heap), "index " + str(index) + " is out of bounds; trying to do stuff with node " + str(element_id)
        self.heap[index].set_key(new_key)
        self.__sift_up(index)

    def __sift_down(self, i):
        # Restores the heap property
        while self.__child(i, 1) < self.size:
            min_child = self.__min_child(i)
            if self.heap[i] > self.heap[min_child]:
                self.__swap(i, min_child)
                i = min_child
            else:
                break

    def __min_child(self, i):
        # Returns the smallest child for the given index
        min_child = self.__child(i, 1)
        for j in range(2, self.k + 1):
            if self.__child(i, j) < self.size and self.heap[self.__child(i, j)] < self.heap[min_child]:
                min_child = self.__child(i, j)
        return min_child

    def contains(self, element_id):
        # Checks if element is in the heap
        return (element_id in self.element_index)

    def remove(self, element_id):
        # Deletes an element from the heap
        if (not self.contains(element_id) and not self.empty()):
            return

        self.decreaseKey(element_id, float("-inf"))
        self.extract_min()
        
    def is_heap(self):
        # Returns true if the heap fullfills the heap property
        for i in range(1, self.size):
            parent = self.__parent(i)
            if self.heap[parent] > self.heap[i]:
                return False
        return True
        
    def __str__(self):
        return ", ".join([str(e) for e in self.heap])
