# Unit 4 — Sorting & Binary Search

## 1. Why sorting matters even though you'll rarely hand-write a sort

In interviews you almost never implement quicksort/mergesort from scratch —
you call `sorted()` or `.sort()`. What matters is:
- Knowing the complexity cost you're paying when you sort (`O(n log n)` time,
  and whether it's in-place or not).
- Recognizing when sorting *unlocks* an easier algorithm afterward (you've
  already seen this: Two Sum II / Three Sum in Unit 2 both relied on sorting
  first to enable two-pointer convergence).
- Knowing `sorted(iterable, key=..., reverse=...)` cold — the `key` argument
  especially, since "sort by some derived value, not the raw value" comes up
  constantly (you used this exact idea with `heapq.nlargest`'s `key` param
  in Unit 3).

Python's `sorted()` / `list.sort()` are Timsort — `O(n log n)` worst case,
stable (equal elements keep their relative order, which matters when you
sort by a secondary key after a primary one).

## 2. Binary search — the core idea

Binary search works on any sequence where you can answer "is the answer to
my left or right of this midpoint?" in O(1) — classically a **sorted**
array, but the same shape applies to "search a range of possible answers"
problems (you'll see this generalization in Level 2+).

The reliable template — memorize this exact shape, not a variant:

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1  # not found
```

Key details that are easy to get wrong (you already hit the insert-position
version of this bug in Unit 1's checkpoint):
- Loop condition is `lo <= hi`, **not** `lo < hi` — using `<` silently skips
  checking the case where the search space is exactly one element.
- `mid = (lo + hi) // 2` — for huge arrays in other languages this can
  overflow; irrelevant in Python, but know why some codebases write
  `lo + (hi - lo) // 2` instead.
- When the loop exits without finding the target, `lo` has converged to the
  correct **insertion point** — this generalizes binary search beyond
  "find exact match" to "find where this belongs" (`bisect.insort` territory).

## 3. Binary search on the *answer*, not the array

A pattern that trips people up the first time: sometimes the array you
binary-search over isn't literally the input — it's implicit. Example: "find
the smallest value X such that condition(X) is true," where `condition` is
monotonic (once true, stays true for all larger X). You binary search over
*possible values of X*, calling `condition(mid)` instead of comparing
`arr[mid]` to a target. You won't need this until a later problem in this
unit, but the shape is identical to the template above once you see it.

## 4. Sorting-adjacent patterns worth knowing

- **Merge two sorted lists/arrays** — two-pointer merge, `O(n + m)`. Shows up
  standalone and as the core subroutine of merge sort.
- **Quickselect** (partition-based "find the kth smallest/largest without
  fully sorting") — average `O(n)`, a nice alternative to the heap approach
  from Unit 3's Top-K problem. You'll meet this as an optional stretch goal.
- `bisect` module (`bisect_left`, `bisect_right`, `insort`) — Python's
  built-in binary search on sorted sequences. Worth knowing it exists even
  if you implement binary search by hand in interviews (some interviewers
  are fine with you using it, some want to see you write it — ask).
