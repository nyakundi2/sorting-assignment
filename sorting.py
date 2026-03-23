"""
Sorting Algorithms Assignment
Student: Boaz Ombati Nyakundi
Reg No:  EB3/67333/23

Implements Bubble Sort and Insertion Sort without built-in sorting functions.
Tracks comparisons and swaps, and runs experiments on lists of various sizes.
"""

import random
import time


# ─────────────────────────────────────────────
#  BUBBLE SORT
# ─────────────────────────────────────────────

def bubble_sort(arr, ascending=True):
    """
    Bubble Sort: repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. The largest (or smallest)
    element 'bubbles' to its correct position after each full pass.

    Returns: (sorted list, comparisons count, swaps count)
    """
    data = arr[:]          # work on a copy
    n = len(data)
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            # Decide swap direction based on sort order
            should_swap = data[j] > data[j + 1] if ascending else data[j] < data[j + 1]
            if should_swap:
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps += 1
                swapped = True
        if not swapped:          # early exit if already sorted
            break

    return data, comparisons, swaps


# ─────────────────────────────────────────────
#  INSERTION SORT
# ─────────────────────────────────────────────

def insertion_sort(arr, ascending=True):
    """
    Insertion Sort: builds the sorted list one element at a time.
    Each new element is inserted into its correct position among the
    already-sorted elements to its left, by shifting larger elements right.

    Returns: (sorted list, comparisons count, swaps count)
    """
    data = arr[:]
    n = len(data)
    comparisons = 0
    swaps = 0

    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            should_move = data[j] > key if ascending else data[j] < key
            if should_move:
                data[j + 1] = data[j]   # shift element one position right
                swaps += 1
                j -= 1
            else:
                break
        data[j + 1] = key

    return data, comparisons, swaps


# ─────────────────────────────────────────────
#  STEP-BY-STEP DEMONSTRATION
# ─────────────────────────────────────────────

def demo_bubble_sort(arr):
    """Show step-by-step passes of Bubble Sort on a small list."""
    data = arr[:]
    n = len(data)
    print("\n=== Bubble Sort Step-by-Step ===")
    print(f"  Input : {data}")
    step = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                step += 1
                print(f"  Swap #{step}: swapped index {j} and {j+1} → {data}")
        if not swapped:
            print(f"  Pass {i+1}: no swaps needed, list is sorted early.")
            break
        else:
            print(f"  End of pass {i+1}: {data}")
    print(f"  Result: {data}")


def demo_insertion_sort(arr):
    """Show step-by-step insertions of Insertion Sort on a small list."""
    data = arr[:]
    n = len(data)
    print("\n=== Insertion Sort Step-by-Step ===")
    print(f"  Input : {data}")
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        print(f"  Inserted {key} → {data}")
    print(f"  Result: {data}")


# ─────────────────────────────────────────────
#  EXPERIMENT RUNNER
# ─────────────────────────────────────────────

SIZES = [1, 2, 3, 4, 5, 10, 250, 999, 9999, 89786, 789300, 1780000]

def run_experiments():
    """Run both algorithms on lists of various sizes and print results."""
    print("\n" + "=" * 90)
    print("EXPERIMENT RESULTS")
    print("=" * 90)
    header = f"{'Size':>10} | {'Algorithm':>14} | {'Time (s)':>10} | {'Comparisons':>14} | {'Swaps':>14}"
    print(header)
    print("-" * 90)

    for size in SIZES:
        data = [random.randint(1, 1_000_000) for _ in range(size)]

        # ── Bubble Sort ──
        if size <= 100_000:   # skip very large for bubble sort (too slow)
            start = time.perf_counter()
            _, comps, swps = bubble_sort(data)
            elapsed = time.perf_counter() - start
            print(f"{size:>10} | {'Bubble Sort':>14} | {elapsed:>10.4f} | {comps:>14,} | {swps:>14,}")
        else:
            print(f"{size:>10} | {'Bubble Sort':>14} | {'SKIPPED (too slow)':>42}")

        # ── Insertion Sort ──
        if size <= 500_000:
            start = time.perf_counter()
            _, comps, swps = insertion_sort(data)
            elapsed = time.perf_counter() - start
            print(f"{size:>10} | {'Insertion Sort':>14} | {elapsed:>10.4f} | {comps:>14,} | {swps:>14,}")
        else:
            print(f"{size:>10} | {'Insertion Sort':>14} | {'SKIPPED (too slow)':>42}")

        print("-" * 90)


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    # ── 1. Demo on a small unsorted list ──────────────────────────────────
    sample = [64, 25, 12, 22, 11]
    print("╔══════════════════════════════════════╗")
    print("║        SORTING ALGORITHMS DEMO       ║")
    print("╚══════════════════════════════════════╝")
    print(f"\nUnsorted list: {sample}")

    demo_bubble_sort(sample)
    demo_insertion_sort(sample)

    # ── 2. Sort ascending and show stats ──────────────────────────────────
    print("\n=== Sorting Ascending ===")
    sorted_b, c_b, s_b = bubble_sort(sample)
    print(f"  Bubble Sort    → {sorted_b}  | Comparisons: {c_b} | Swaps: {s_b}")

    sorted_i, c_i, s_i = insertion_sort(sample)
    print(f"  Insertion Sort → {sorted_i}  | Comparisons: {c_i} | Swaps: {s_i}")

    # ── 3. Sort descending ────────────────────────────────────────────────
    print("\n=== Sorting Descending ===")
    sorted_b_d, c_b_d, s_b_d = bubble_sort(sample, ascending=False)
    print(f"  Bubble Sort    → {sorted_b_d}  | Comparisons: {c_b_d} | Swaps: {s_b_d}")

    sorted_i_d, c_i_d, s_i_d = insertion_sort(sample, ascending=False)
    print(f"  Insertion Sort → {sorted_i_d}  | Comparisons: {c_i_d} | Swaps: {s_i_d}")

    # ── 4. Accept user input ───────────────────────────────────────────────
    print("\n─────────────────────────────────────────")
    user_input = input("Enter your own integers separated by spaces (or press Enter to skip): ").strip()
    if user_input:
        try:
            user_list = list(map(int, user_input.split()))
            sorted_u, c_u, s_u = bubble_sort(user_list)
            print(f"  Sorted (Bubble): {sorted_u}")
            print(f"  Comparisons: {c_u} | Swaps: {s_u}")
        except ValueError:
            print("  Invalid input — skipping.")

    # ── 5. Experiments ────────────────────────────────────────────────────
    run_experiments()


if __name__ == "__main__":
    main()
