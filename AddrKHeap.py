"""
Copyright 2023 Patrick Steil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from dataclasses import dataclass, field
from typing import Dict, Optional, List


@dataclass
class HeapElement:
    key: int
    element_id: int
    index: int = field(default=0)


class AddrKHeap:
    def __init__(self, k: int = 4):
        assert k >= 2
        self.k = k
        self.heap: List[HeapElement] = []
        self.size = 0
        self.element_index: Dict[int, int] = {}

    def empty(self) -> bool:
        return self.size == 0

    def get_size(self) -> int:
        return self.size

    def __parent(self, i: int) -> int:
        return (i - 1) // self.k

    def __child(self, i: int, j: int) -> int:
        return self.k * i + j

    def insert(self, element_id: int, key: int) -> None:
        element = HeapElement(key, element_id, self.size)
        self.heap.append(element)
        self.element_index[element_id] = self.size
        self.size += 1
        self.__sift_up(self.size - 1)

    def __swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.element_index[self.heap[i].element_id] = i
        self.element_index[self.heap[j].element_id] = j

    def __sift_up(self, i: int) -> None:
        while i > 0:
            parent = self.__parent(i)
            if self.heap[parent].key > self.heap[i].key:
                self.__swap(parent, i)
                i = parent
            else:
                break

    def front_key(self) -> Optional[int]:
        return self.heap[0].key if not self.empty() else None

    def front_element_id(self) -> Optional[int]:
        return self.heap[0].element_id if not self.empty() else None

    def extract_min(self) -> Optional[HeapElement]:
        if self.size == 0:
            return None
        min_element = self.heap[0]
        self.size -= 1
        last_element = self.heap.pop()  # Pops last element
        if self.size > 0:
            self.heap[0] = last_element
            last_element.index = 0
            self.element_index[last_element.element_id] = 0
            self.__sift_down(0)
        del self.element_index[min_element.element_id]
        return min_element

    def deleteMinNode(self) -> Optional[int]:
        min_extract = self.extract_min()
        return min_extract.element_id if min_extract else None

    def update(self, element_id: int, new_key: int) -> None:
        if not self.contains(element_id):
            self.insert(element_id, new_key)
        else:
            self.decreaseKey(element_id, new_key)

    def decreaseKey(self, element_id: int, new_key: int) -> None:
        if not self.contains(element_id):
            return

        index = self.element_index[element_id]
        self.heap[index].key = new_key
        self.__sift_up(index)

    def __sift_down(self, i: int) -> None:
        while True:
            min_child = self.__min_child(i)
            if min_child is None or self.heap[i].key <= self.heap[min_child].key:
                break
            self.__swap(i, min_child)
            i = min_child

    def __min_child(self, i: int) -> Optional[int]:
        min_index = None
        for j in range(1, self.k + 1):
            child_index = self.__child(i, j)
            if child_index < self.size:
                if (
                    min_index is None
                    or self.heap[child_index].key < self.heap[min_index].key
                ):
                    min_index = child_index
        return min_index

    def contains(self, element_id: int) -> bool:
        return element_id in self.element_index

    def remove(self, element_id: int) -> None:
        if not self.contains(element_id):
            return

        self.decreaseKey(element_id, float("-inf"))
        self.extract_min()

    def is_heap(self) -> bool:
        for i in range(1, self.size):
            parent = self.__parent(i)
            if self.heap[parent].key > self.heap[i].key:
                return False
        return True

    def __str__(self) -> str:
        return ", ".join(str(e) for e in self.heap)
