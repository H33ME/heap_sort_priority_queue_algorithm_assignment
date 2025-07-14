# heap_sort_priority_queue.py

import random
import time

# ----------------------------
# HEAPSORT IMPLEMENTATION
# ----------------------------
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# ----------------------------
# PRIORITY QUEUE IMPLEMENTATION
# ----------------------------
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task({self.task_id}, priority={self.priority})"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        l, r = 2 * index + 1, 2 * index + 2
        if l < len(self.heap) and self.heap[l] > self.heap[largest]:
            largest = l
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def increase_priority(self, task_id, new_priority):
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority > task.priority:
                    task.priority = new_priority
                    self._heapify_up(i)
                break

    def is_empty(self):
        return len(self.heap) == 0

# ----------------------------
# COMPARISON FUNCTION
# ----------------------------
def compare_sorting_algorithms():
    from time import time
    import matplotlib.pyplot as plt
    import copy

    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            merge_sort(L)
            merge_sort(R)

            i = j = k = 0

            # Merge the temp arrays back into arr
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Copy any remaining elements of L
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            # Copy any remaining elements of R
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1


    def quicksort(arr):
        if len(arr) <= 1: return arr
        pivot = arr[0]
        return quicksort([x for x in arr[1:] if x <= pivot]) + [pivot] + quicksort([x for x in arr[1:] if x > pivot])

    sizes = [100, 1000, 5000, 10000]
    results = {'heapsort': [], 'mergesort': [], 'quicksort': []}

    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]

        for name, func in [('heapsort', heapsort), ('mergesort', merge_sort), ('quicksort', quicksort)]:
            temp = copy.deepcopy(arr)
            start = time()
            func(temp)
            end = time()
            results[name].append(end - start)

    plt.figure(figsize=(10, 6))
    for algo, times in results.items():
        plt.plot(sizes, times, label=algo)
    plt.xlabel('Input Size')
    plt.ylabel('Time (s)')
    plt.title('Sorting Algorithm Comparison')
    plt.legend()
    plt.grid(True)
    plt.savefig('sorting_comparison.png')
    plt.show()

# ----------------------------
# MAIN ENTRY
# ----------------------------
if __name__ == "__main__":
    print("--- Heapsort Test ---")
    arr = [4, 10, 3, 5, 1]
    heapsort(arr)
    print("Sorted:", arr)

    print("\n--- Priority Queue Test ---")
    pq = PriorityQueue()
    pq.insert(Task("A", 3, 0, 10))
    pq.insert(Task("B", 5, 1, 8))
    pq.insert(Task("C", 1, 2, 12))
    print("Extracted:", pq.extract_max())
    pq.increase_priority("C", 6)
    print("Extracted after increase:", pq.extract_max())

    print("\n--- Sorting Comparison ---")
    compare_sorting_algorithms()
