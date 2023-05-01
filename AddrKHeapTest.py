from AddrKHeap import AddrKHeap
import random

N = 1000

# Test case 1: Test insert and the heap property
def test_addrkheap_insert_and_min_heap_property(k):
    heap = AddrKHeap(k)
    for i in range(N):
        heap.insert(i, random.randint(-1000, 1000))
    assert heap.is_heap()

# Test case 2: Test extract_min method and min-heap property
def test_addrkheap_extract_min_and_min_heap_property(k):
    heap = AddrKHeap(k)
    elements = [random.randint(-1000, 1000) for i in range(N)]
    for i in range(len(elements)):
        heap.insert(i, elements[i])
    sorted_elements = sorted(elements)
    for i in range(heap.get_size()):
        assert heap.extract_min().get_key() == sorted_elements[i]
        assert heap.is_heap()

# Test case 3: Test that extracting from an empty heap returns None
def test_addrkheap_extract_from_empty_heap(k):
    heap = AddrKHeap(k)
    assert heap.extract_min() == None

# Test case 4: Test that decreaseKey works properly
def test_addrkheap_decreaseKey(k):
    heap = AddrKHeap(k)
    for i in range(N):
        heap.insert(i, random.randint(-1000, 1000))

    heap.decreaseKey(100, -2000)
    assert heap.is_heap()
    assert heap.front_key() == -2000 and heap.front_element_id() == 100
    heap.extract_min()

    heap.decreaseKey(200, -2000)
    assert heap.is_heap()
    assert heap.front_key() == -2000 and heap.front_element_id() == 200

# Test case 5: Test that remove works properly
def test_addrkheap_remove(k):
    heap = AddrKHeap(k)
    for i in range(10):
        heap.insert(i, random.randint(-1000, 1000))

    while (not heap.empty()):
        heap.remove(heap.front_element_id())
        assert heap.is_heap()


ks = [2, 4, 8, 16]

for k in ks:
    test_addrkheap_insert_and_min_heap_property(k)
    test_addrkheap_extract_min_and_min_heap_property(k)
    test_addrkheap_extract_from_empty_heap(k)
    test_addrkheap_decreaseKey(k)
    test_addrkheap_remove(k)

print("All test cases passed!")