import random
import unittest
from AddrKHeap import AddrKHeap

N = 1000


class TestAddrKHeap(unittest.TestCase):

    def test_insert_and_min_heap_property(self):
        ks = [2, 4, 8, 16]
        for k in ks:
            heap = AddrKHeap(k)
            for i in range(N):
                heap.insert(i, random.randint(-1000, 1000))
            self.assertTrue(heap.is_heap(), f"Heap property violated for k={k}")

    def test_extract_min_and_min_heap_property(self):
        ks = [2, 4, 8, 16]
        for k in ks:
            heap = AddrKHeap(k)
            elements = [random.randint(-1000, 1000) for _ in range(N)]
            for i in range(len(elements)):
                heap.insert(i, elements[i])
            sorted_elements = sorted(elements)
            for i in range(heap.get_size()):
                self.assertEqual(
                    heap.extract_min().key,
                    sorted_elements[i],
                    f"Extract min failed for k={k}",
                )
                self.assertTrue(
                    heap.is_heap(),
                    f"Heap property violated after extract min for k={k}",
                )

    def test_extract_from_empty_heap(self):
        ks = [2, 4, 8, 16]
        for k in ks:
            heap = AddrKHeap(k)
            self.assertIsNone(
                heap.extract_min(), f"Expected None for empty heap for k={k}"
            )

    def test_decreaseKey(self):
        ks = [2, 4, 8, 16]
        for k in ks:
            heap = AddrKHeap(k)
            for i in range(N):
                heap.insert(i, random.randint(-1000, 1000))

            heap.decreaseKey(100, -2000)
            self.assertTrue(
                heap.is_heap(), f"Heap property violated after decreaseKey for k={k}"
            )
            self.assertEqual(heap.front_key(), -2000)
            self.assertEqual(heap.front_element_id(), 100)
            heap.extract_min()

            heap.decreaseKey(200, -2000)
            self.assertTrue(
                heap.is_heap(), f"Heap property violated after decreaseKey for k={k}"
            )
            self.assertEqual(heap.front_key(), -2000)
            self.assertEqual(heap.front_element_id(), 200)

    def test_remove(self):
        ks = [2, 4, 8, 16]
        for k in ks:
            heap = AddrKHeap(k)
            for i in range(10):
                heap.insert(i, random.randint(-1000, 1000))

            while not heap.empty():
                heap.remove(heap.front_element_id())
                self.assertTrue(
                    heap.is_heap(), f"Heap property violated after remove for k={k}"
                )


if __name__ == "__main__":
    unittest.main()
