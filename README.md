# Sorting Algorithms Assignment

## Student Information
- **Name:** Boaz Ombati Nyakundi
- **Registration Number:** EB3/67333/23

---

## Description of Sorting Algorithms

This project implements **two classic sorting algorithms** from scratch in Python —
**Bubble Sort** and **Insertion Sort** — without using any built-in sorting functions.
Both algorithms sort a list of integers in ascending or descending order, and track
the total number of comparisons and swaps performed.

---

## How to Run

```bash
python3 sorting.py
```

You will be prompted to enter your own list of integers, and both algorithms will
sort them and display the statistics. Experiment results across various list sizes
are printed automatically.

---

## Experiment Results

### 4. Comparisons and Swaps Performed

The table below shows real measured results on randomly generated lists:

| Size  | Algorithm      | Time (s) | Comparisons    | Swaps          |
|-------|----------------|----------|----------------|----------------|
| 1     | Bubble Sort    | ~0.0000  | 0              | 0              |
| 1     | Insertion Sort | ~0.0000  | 0              | 0              |
| 2     | Bubble Sort    | ~0.0000  | 1              | 0              |
| 2     | Insertion Sort | ~0.0000  | 1              | 0              |
| 3     | Bubble Sort    | ~0.0000  | 3              | 1              |
| 3     | Insertion Sort | ~0.0000  | 2              | 1              |
| 4     | Bubble Sort    | ~0.0000  | 6              | 6              |
| 4     | Insertion Sort | ~0.0000  | 6              | 6              |
| 5     | Bubble Sort    | ~0.0000  | 10             | 4              |
| 5     | Insertion Sort | ~0.0000  | 8              | 4              |
| 10    | Bubble Sort    | ~0.0000  | 45             | 23             |
| 10    | Insertion Sort | ~0.0000  | 29             | 23             |
| 250   | Bubble Sort    | 0.0028   | 31,122         | 14,632         |
| 250   | Insertion Sort | 0.0012   | 14,878         | 14,632         |
| 999   | Bubble Sort    | 0.0487   | 497,973        | 259,800        |
| 999   | Insertion Sort | 0.0233   | 260,795        | 259,800        |
| 9,999 | Bubble Sort    | 5.49     | 49,954,125     | 25,288,173     |
| 9,999 | Insertion Sort | 2.35     | 25,298,162     | 25,288,173     |
| 89,786    | Bubble Sort    | N/A (too slow) | ~4.04 billion (est.) | ~2.02 billion (est.) |
| 89,786    | Insertion Sort | ~1,060 s (est.)| ~2.02 billion (est.) | ~2.02 billion (est.) |
| 789,300   | Both           | Impractical in pure Python | ~3.1 × 10¹¹ (est.) | — |
| 1,780,000 | Both           | Impractical in pure Python | ~1.58 × 10¹²(est.) | — |

> **Note:** For very large lists (89,786+), estimates are based on the O(n²) formula.
> Both algorithms become impractical for production use beyond ~10,000 elements.
> Real-world applications use O(n log n) algorithms like Merge Sort or Tim Sort.

---

### 5. How Each Sorting Algorithm Works

#### Bubble Sort

Bubble Sort works by making repeated passes through the list. On each pass, it
compares every pair of adjacent elements. If two adjacent elements are in the
wrong order, it swaps them. After the first full pass, the largest element has
"bubbled up" to the last position. After the second pass, the second-largest is
in its correct place, and so on.

An important optimization is the **early exit**: if a complete pass is made with
no swaps, the list is already sorted and the algorithm stops immediately. This is
what gives Bubble Sort its O(n) best case on already-sorted input.

```
Pass 1: [64, 25, 12, 22, 11]
  Compare 64 & 25 → swap → [25, 64, 12, 22, 11]
  Compare 64 & 12 → swap → [25, 12, 64, 22, 11]
  Compare 64 & 22 → swap → [25, 12, 22, 64, 11]
  Compare 64 & 11 → swap → [25, 12, 22, 11, 64]
Pass 2: 64 is fixed; process first 4 elements, etc.
```

#### Insertion Sort

Insertion Sort builds a sorted sub-list one element at a time, starting from the
second element. For each new element (the "key"), it looks backwards through the
already-sorted portion to find the correct position. Elements that are larger than
the key are shifted one position to the right to make room. Once the correct
position is found, the key is placed there.

Think of it like sorting a hand of playing cards: you pick up one card at a time
and slide it left into the right position among the cards you are already holding.

```
Start: [64, 25, 12, 22, 11]
i=1, key=25: 64 > 25, shift right → insert 25 → [25, 64, 12, 22, 11]
i=2, key=12: 64 > 12, shift; 25 > 12, shift → insert 12 → [12, 25, 64, 22, 11]
i=3, key=22: 64 > 22, shift; 25 > 22, shift; 12 ≤ 22 → insert → [12, 22, 25, 64, 11]
i=4, key=11: shift all → [11, 12, 22, 25, 64]
```

---

### 6. Step-by-Step Example

**Input list:** `[64, 25, 12, 22, 11]`

#### Bubble Sort (Ascending)

| Pass | Action                              | List State              |
|------|-------------------------------------|-------------------------|
| 1    | Swap 64 & 25                        | [25, 64, 12, 22, 11]   |
| 1    | Swap 64 & 12                        | [25, 12, 64, 22, 11]   |
| 1    | Swap 64 & 22                        | [25, 12, 22, 64, 11]   |
| 1    | Swap 64 & 11                        | [25, 12, 22, 11, 64]   |
| 2    | Swap 25 & 12                        | [12, 25, 22, 11, 64]   |
| 2    | Swap 25 & 22                        | [12, 22, 25, 11, 64]   |
| 2    | Swap 25 & 11                        | [12, 22, 11, 25, 64]   |
| 3    | No swap 12 & 22; Swap 22 & 11       | [12, 11, 22, 25, 64]   |
| 4    | Swap 12 & 11                        | [11, 12, 22, 25, 64]   |
| **Final** | **Result**                   | **[11, 12, 22, 25, 64]** |

Total: **10 comparisons**, **8 swaps**

#### Insertion Sort (Ascending)

| Step | Key | Action                              | List State              |
|------|-----|-------------------------------------|-------------------------|
| i=1  | 25  | 64 > 25 → shift 64 right            | [25, 64, 12, 22, 11]   |
| i=2  | 12  | 64>12, 25>12 → shift both           | [12, 25, 64, 22, 11]   |
| i=3  | 22  | 64>22, 25>22; 12≤22 → insert        | [12, 22, 25, 64, 11]   |
| i=4  | 11  | All > 11 → shift all; insert at 0   | [11, 12, 22, 25, 64]   |
| **Final** | **Result**                   | **[11, 12, 22, 25, 64]** |

Total: **10 comparisons**, **8 swaps**

---

### 7. Time Complexity Analysis

#### Bubble Sort

| Case        | Condition                    | Comparisons      | Swaps       | Big-O     |
|-------------|------------------------------|------------------|-------------|-----------|
| Best Case   | Already sorted (early exit)  | n − 1            | 0           | **O(n)**  |
| Average Case| Random order                 | ≈ n²/2           | ≈ n²/4      | **O(n²)** |
| Worst Case  | Reverse sorted               | n(n−1)/2         | n(n−1)/2    | **O(n²)** |

**Reasoning:** The outer loop runs up to n−1 times. The inner loop runs up to
n−1−i times per pass. In the worst case (fully reversed list), every adjacent
pair needs to be swapped on every pass, giving n(n−1)/2 ≈ n²/2 operations.
In the best case, the first pass completes with no swaps, and the algorithm exits
after just n−1 comparisons.

#### Insertion Sort

| Case        | Condition                    | Comparisons      | Shifts      | Big-O     |
|-------------|------------------------------|------------------|-------------|-----------|
| Best Case   | Already sorted               | n − 1            | 0           | **O(n)**  |
| Average Case| Random order                 | ≈ n²/4           | ≈ n²/4      | **O(n²)** |
| Worst Case  | Reverse sorted               | n(n−1)/2         | n(n−1)/2    | **O(n²)** |

**Reasoning:** For each element at position i, Insertion Sort may look back
through all i previously sorted elements in the worst case. Summing over all
positions: 1+2+3+…+(n−1) = n(n−1)/2. In the best case (sorted input), each
new element is already in place, requiring only one comparison per element (n−1
total comparisons, 0 shifts).

**Key difference:** Insertion Sort typically does roughly **half as many
comparisons** as Bubble Sort on random data, because it stops comparing as soon
as it finds the correct insertion point (no unnecessary comparisons after
finding the spot). The experiment data confirms this: at n=999, Bubble Sort
made 497,973 comparisons while Insertion Sort made only 260,795.

---

### 8. Space Complexity

| Algorithm      | Space Complexity | Explanation |
|----------------|-----------------|-------------|
| Bubble Sort    | **O(1)**        | Sorts in-place. Only a fixed number of extra variables are used (loop counters, a temp variable for swapping), regardless of input size. |
| Insertion Sort | **O(1)**        | Also sorts in-place. The `key` variable holds one element at a time, and the shifting of elements uses the existing array space. No extra array is needed. |

Both algorithms are **in-place** sorting algorithms. No auxiliary arrays are
allocated. The memory used does not grow as the input size grows. This contrasts
with algorithms like Merge Sort, which requires O(n) additional space.

---

### 9. Discussion: Performance at Scale

From the experiment results:

1. **Small lists (n ≤ 10):** Both algorithms complete in microseconds.
   The number of comparisons and swaps is tiny and nearly identical.

2. **Medium lists (n = 250 – 999):** Insertion Sort is approximately **2×
   faster** than Bubble Sort because it performs roughly half the comparisons.
   Bubble Sort visits every pair in the unsorted region on every pass, while
   Insertion Sort stops early once the correct position is found.

3. **Large lists (n = 9,999):** Bubble Sort takes ~5.5 seconds vs ~2.4 seconds
   for Insertion Sort. The quadratic growth is clearly visible — going from
   n=999 to n=9,999 (10× larger) increases time by approximately 100×, exactly
   as predicted by O(n²).

4. **Very large lists (n ≥ 89,786):** Both algorithms are impractical.
   At n=89,786, the estimated operation count exceeds **4 billion** for Bubble
   Sort and ~2 billion for Insertion Sort. At 1.78 million elements, estimates
   reach **~1.58 trillion operations** — clearly unusable for real applications.

**Conclusion:** Both Bubble Sort and Insertion Sort are excellent for teaching
algorithm concepts and work well on small lists (< ~1,000 elements). Insertion
Sort is consistently faster than Bubble Sort in practice due to its early
termination within each inner-loop iteration. For production use on large datasets,
an O(n log n) algorithm (Merge Sort, Quick Sort, or Python's built-in Tim Sort)
should always be preferred.

---

## Repository Structure

```
sorting-assignment/
├── sorting.py     # Main program (both algorithms, demo, experiments)
└── README.md      # This file
```

---

## Submission

`EB3/67333/23 – Boaz Ombati Nyakundi – [Link to Repository]`
