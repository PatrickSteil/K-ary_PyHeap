"""
Copyright 2023 Patrick Steil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import array
from typing import List, Optional


class KHeap:
    def __init__(self, k: int = 4):
        assert k >= 2, "k must be at least 2"
        self.k: int = k
        self.heap: array.array = array.array("l")
        self.size: int = 0

    def empty(self) -> bool:
        """Returns True if the heap is empty."""
        return self.size == 0

    def get_size(self) -> int:
        """Returns the number of elements in the heap."""
        return self.size

    def __parent(self, index: int) -> int:
        """Returns the index of the parent of the given index."""
        return (index - 1) // self.k

    def __child(self, index: int, child_index: int) -> int:
        """Returns the index of the child of the given index."""
        return self.k * index + child_index

    def insert(self, key: int) -> None:
        """Inserts a new key into the heap."""
        self.heap.append(key)
        self.size += 1
        self.__sift_up(self.size - 1)

    def insert_many(self, values: List[int]) -> None:
        """Inserts multiple keys into the heap."""
        self.heap.extend(values)
        self.size += len(values)
        # Sift up only the newly inserted elements
        for i in range(self.size - len(values), self.size):
            self.__sift_up(i)

    def __sift_up(self, index: int) -> None:
        """Restores the heap property by sifting up the element at the given index."""
        while index > 0:
            parent_index = self.__parent(index)
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = (
                    self.heap[index],
                    self.heap[parent_index],
                )
                index = parent_index
            else:
                break

    def extract_min(self) -> Optional[int]:
        """Removes and returns the smallest key from the heap."""
        if self.empty():
            return None
        min_element = self.heap[0]
        last_element = self.heap.pop()
        self.size -= 1
        if self.size > 0:
            self.heap[0] = last_element
            self.__sift_down(0)
        return min_element

    def __sift_down(self, index: int) -> None:
        """Restores the heap property by sifting down the element at the given index."""
        while True:
            min_child_index = self.__min_child(index)
            if (
                min_child_index is None
                or self.heap[index] <= self.heap[min_child_index]
            ):
                break
            self.heap[index], self.heap[min_child_index] = (
                self.heap[min_child_index],
                self.heap[index],
            )
            index = min_child_index

    def __min_child(self, index: int) -> Optional[int]:
        """Returns the index of the smallest child for the given index."""
        min_index = None
        for j in range(1, self.k + 1):
            child_index = self.__child(index, j)
            if child_index < self.size and (
                min_index is None or self.heap[child_index] < self.heap[min_index]
            ):
                min_index = child_index
        return min_index

    def is_heap(self) -> bool:
        """Checks if the heap maintains the heap property."""
        return all(
            self.heap[self.__parent(i)] <= self.heap[i] for i in range(1, self.size)
        )

    def __str__(self) -> str:
        """Returns a string representation of the heap."""
        return str(self.heap.tolist())  # Convert to list for better readability
