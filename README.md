Here's a complete **README.md** file for your project. It provides instructions on how to run the code, a summary of the report findings, and descriptions of key functionalities.

---

````markdown
# 📊 Performance Evaluation of Heapsort and Priority Queue Using Heap Data Structures

## 📝 Overview

This project implements and analyzes **heap-based data structures**, specifically:

- **Heapsort** — a comparison-based sorting algorithm using a max-heap.
- **Priority Queue** — a dynamic structure using a binary heap to efficiently manage tasks based on priority.

Additionally, the project includes a **performance comparison** between Heapsort, Quicksort, and Mergesort across increasing input sizes.

---

## 📂 Files Included

- `heap_sort_priority_queue.py` – Main script implementing heapsort, priority queue, and sorting comparisons.
- `sorting_comparison.png` – Graph showing the runtime performance of sorting algorithms (generated after execution).
- `README.md` – Project documentation.
- `SAIMAH Algorithms ASSIGNMENT 2.docx` – Full analytical report with theoretical and empirical discussion.

---

## ▶️ How to Run

### 🖥️ Requirements
- Python 3.7+
- `matplotlib` library for plotting

### 🔧 Install Dependencies
If not already installed:
```bash
pip install matplotlib
````

### 🚀 Execute the Script

```bash
python3 heap_sort_priority_queue.py
```

This will:

1. Test the Heapsort implementation and print the sorted result.
2. Test the Priority Queue with tasks and demonstrate insert, extract, and increase-priority operations.
3. Generate and display a plot comparing the runtimes of Heapsort, Quicksort, and Mergesort for increasing input sizes.

The plot will be saved as `sorting_comparison.png`.

---

## 🧪 Functionality Breakdown

### ✅ Heapsort

* In-place implementation using a max-heap.
* Time Complexity: `O(n log n)` in all cases.
* Space Complexity: `O(1)`.

### ✅ Priority Queue (using Binary Heap)

* Core operations:

  * `insert(task)`
  * `extract_max()`
  * `increase_priority(task_id, new_priority)`
  * `is_empty()`
* Each operation has a time complexity of `O(log n)`.

### ✅ Sorting Comparison

* Empirical runtime comparison of:

  * **Heapsort**
  * **Quicksort** (random pivot)
  * **Mergesort**
* Tested on input sizes: 100, 1000, 5000, 10000.
* Outputs runtime graph for each algorithm.

---

## 📈 Key Findings (from Report)

* **Heapsort**: Deterministic `O(n log n)` runtime, space-efficient but slower due to reheapification.
* **Quicksort**: Fastest in practice on random data due to in-place implementation and low overhead.
* **Mergesort**: Stable and consistent `O(n log n)` runtime, but with extra memory usage.
* **Priority Queue**: Efficient for real-time task scheduling, maintaining heap order for fast insert and extraction.

---

## 📚 References

* Tjernström, K. J., & Paulsson, V. (2025). *A Performance Study of Priority Queues: Binary Heap, Fibonacci Heap, Hollow Heap*. LU-CS-EX.
* Meng, S., Zhu, Q., & Xia, F. (2019). *Improvement of the Dynamic Priority Scheduling Algorithm Based on a Heapsort*. IEEE Access.

---
