import random
import unittest
from Heap import KHeap

class TestKHeap(unittest.TestCase):

    def test_insert_and_min_heap_property(self):
        ks = [2, 4, 8, 16]
        for k in ks:
            heap = KHeap(k)
            for _ in range(1000):
                heap.insert(random.randint(-1000, 1000))
            self.assertTrue(heap.is_heap(), f"Heap property violated for k={k}")

    def test_insert_many_and_min_heap_property(self):
        ks = [2, 4, 8, 16]
        for k in ks:
            heap = KHeap(k)
            data = [random.randint(-1000, 1000) for _ in range(1000)]
            heap.insert_many(data)
            self.assertTrue(heap.is_heap(), f"Heap property violated after insert_many for k={k}")

    def test_extract_min_and_min_heap_property(self):
        ks = [2, 4, 8, 16]
        for k in ks:
            heap = KHeap(k)
            elements = [random.randint(-1000, 1000) for _ in range(1000)]
            for element in elements:
                heap.insert(element)
            sorted_elements = sorted(elements)
            for i in range(heap.get_size()):
                self.assertEqual(heap.extract_min(), sorted_elements[i], f"Extract min failed for k={k}")
                self.assertTrue(heap.is_heap(), f"Heap property violated after extract min for k={k}")

    def test_extract_from_empty_heap(self):
        ks = [2, 4, 8, 16]
        for k in ks:
            heap = KHeap(k)
            self.assertIsNone(heap.extract_min(), f"Expected None for empty heap for k={k}")

if __name__ == "__main__":
    unittest.main()

