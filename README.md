
# PythonHeap

## What is a heap [Answer by ChatGPT]

An addressable k-ary heap is a k-ary heap data structure variation that allows efficient manipulation of individual elements within the heap.

  

In a standard k-ary heap, each element is located at a fixed position within an array. To access or modify an element, you must know its index in the array. However, in an addressable k-ary heap, each element is assigned a unique handle or identifier, which can be used to locate and manipulate the element without knowing its index in the array.

  

The handles are typically implemented using a hash table or a binary search tree. When an element is added to the heap, its handle is stored in the hash table or binary search tree, along with a reference to its location in the array. When an element needs to be accessed or modified, its handle looks up its position in the array.

  

This addressability feature allows for efficient updates and deletions of individual elements within the heap, which is useful in applications such as graph algorithms and priority queues. However, it also adds some overhead regarding memory usage and the complexity of the implementation.

  

## What is in this repo

This code defines a class AddrKHeap that implements an addressable k-ary heap. The heap can store HeapElement objects, which have a key attribute and an element_id attribute. The element_id attribute can be used to identify elements in the heap so that they can be updated or removed.

The AddrKHeap class provides the following methods:

-   `__init__(k)`: Initializes the heap with an optional k-ary parameter. k is set to 4 by default.
-   `empty()`: Returns True if the heap is empty, False otherwise.
-   `get_size()`: Returns the number of elements currently in the heap.
-   `insert(element_id, key)`: Inserts a new HeapElement object into the heap with the given key and element_id.
-   `front_key()`: Returns the key of the HeapElement object at the top of the heap, without removing it.
-   `front_element_id()`: Returns the element_id of the HeapElement object at the top of the heap, without removing it.
-   `extract_min()`: Removes and returns the HeapElement object at the top of the heap with the minimum key.
-   `deleteMinNode()`: Removes and returns the element_id of the HeapElement object at the top of the heap with the minimum key.
-   `update(element_id, new_key)`: Updates the key of the HeapElement object with the given element_id to the new key. If no HeapElement with the given element_id exists in the heap, a new HeapElement with the given key and element_id is inserted.
-   `decreaseKey(selement_id, new_key)`: Updates the key of the HeapElement object with the given element_id to the new key. If no HeapElement with the given element_id exists in the heap, nothing happens.
-   `remove(element_id)`: Removes the HeapElement object with the given element_id from the heap.
-   `is_heap()`: Returns True if the heap satisfies the heap property, False otherwise.

The AddrKHeap class uses an array to represent the binary tree structure of the heap. The elements in the array are indexed according to the level-order traversal of the binary tree, starting at index 0 for the root node. The `__parent` and `__child` methods are used to calculate the indices of a node's parent and children in the array. The `__sift_up` and `__sift_down` methods are used to restore the heap property after insertions and deletions. The element_index dictionary is used to map element_id values to the indices of the corresponding HeapElement objects in the heap array. This allows for constant-time updates and removals of elements by their element_id values.

## Dijkstra Example
Here is a (very easy and untuned) Dijkstra example.
````
from AddrKHeap import AddrKHeap


G = {
	'A': [('B', 10), ('C', 20)],
	'B': [('C', 5), ('E', 100)],
	'C': [('D', 10)],
	'D': [('E', 15)],
	'E': []
}


Q = AddrKHeap()
Q.insert('A', 0)

visited = set()
distances = {node: float("inf") for node in list(G.keys())}

distances['A'] = 0

while (not Q.empty()):
	node = Q.deleteMinNode()
	visited.add(node)

	for (to, weight) in G[node]:
		if (to in visited):
			continue

		if (distances[node] + weight < distances[to]):
			distances[to] = distances[node] + weight

			Q.update(to, distances[to])

print(distances)
````

This yields `{'A': 0, 'B': 10, 'C': 15, 'D': 25, 'E': 40}`.
