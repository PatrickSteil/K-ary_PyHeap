from Heap import KHeap
import random

# Test case 1: Test insert method and min-heap property
def test_kheap_insert_and_min_heap_property(k):
    heap = KHeap(k)
    for i in range(1000):
        heap.insert(random.randint(-1000, 1000))
    assert heap.is_heap()

# Test case 2: Test extract_min method and min-heap property
def test_kheap_extract_min_and_min_heap_property(k):
    heap = KHeap(k)
    elements = [random.randint(-1000, 1000) for i in range(1000)]
    for element in elements:
        heap.insert(element)
    sorted_elements = sorted(elements)
    for i in range(heap.get_size()):
        assert heap.extract_min() == sorted_elements[i]
        assert heap.is_heap()

# Test case 3: Test that extracting from an empty heap returns None
def test_kheap_extract_from_empty_heap(k):
    heap = KHeap(k)
    assert heap.extract_min() == None


ks = [2, 4, 8, 16]

for k in ks:
    test_kheap_insert_and_min_heap_property(k)
    test_kheap_extract_min_and_min_heap_property(k)
    test_kheap_extract_from_empty_heap(k)

print("All test cases passed!")