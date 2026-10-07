# Unit 2 — Two Pointers & Sliding Window

You already used both patterns informally in Unit 1 (palindrome check,
move zeroes, dedup). This unit makes them explicit, names their variants,
and pushes into cases where the window's *size* isn't fixed — which is
where most people first get stuck.

## 1. Two pointers — the two distinct shapes

**Shape A: Opposite ends, converging inward.**
Used when the array/string is sorted (or order doesn't matter) and you're
looking for a pair/condition involving both extremes. You already did this
in `is_palindrome`. Loop while `left < right`, move one or both pointers
based on a comparison, stop when they meet or cross.

**Shape B: Same direction, different speeds (slow/fast).**
Used for in-place rewriting or detecting structure as you scan once.
You did this in `move_zeroes` and `remove_duplicates`. One pointer (fast)
reads every element; the other (slow) marks where to write next, only
advancing under some condition.

**How to recognize which shape a problem wants:** if the problem involves
comparing/combining elements from *both ends* of a sorted structure (pair
sums, container/area problems, palindromes) → Shape A. If the problem is
about filtering/compacting/rewriting a single array in one direction
(dedup, partitioning, removing elements) → Shape B.

## 2. Sliding window — two pointers that both move forward

A sliding window is really Shape B two-pointers with an extra idea: you
maintain a *window* `[left, right]` representing a contiguous subarray or
substring, and you track some running state about what's currently inside
it (a sum, a count, a set of seen characters). There are two kinds:

**Fixed-size window:** the window size `k` is given. Slide it one step at
a time: add the new element entering on the right, remove the element
leaving on the left, update your running state in O(1) per step instead of
recomputing it from scratch. This turns an O(n·k) brute force into O(n).

**Variable-size window:** you don't know the window size in advance — you
grow `right` to expand the window, and shrink from `left` whenever the
window violates some condition (sum too big, too many distinct characters,
etc.). The key insight that makes this O(n) and not O(n²): **`left` only
ever moves forward, never resets to the start.** Each position is visited
by `right` once and by `left` at most once, so total work across the whole
run is O(n), even though it looks like a nested loop.

**The template to internalize** (variable window, "shrink while invalid"):
```
left = 0
window_state = <empty>
best = <initial>
for right in range(len(arr)):
    add arr[right] to window_state
    while window_state violates the condition:
        remove arr[left] from window_state
        left += 1
    update best using current window [left, right]
```
Almost every variable-window problem is this skeleton with a different
"add," "violates," and "update best."

## 3. Why these patterns matter for interviews specifically

Two pointers and sliding window are the single most common way an O(n²)
brute force (check every pair, or every substring) gets optimized to O(n)
or O(n log n). When you catch yourself writing nested loops over the same
array, the first question should be: "can one of these two pointers move
monotonically instead of resetting?" If yes, you likely have a two-pointer
or sliding-window solution available.

## What you'll practice in this unit

Fixed-window sums, a classic variable-window substring problem, a
shrink-while-valid variant, opposite-end two pointers on an unsorted
array, and a three-pointer extension (two pointers nested inside a single
outer loop) — which previews a pattern you'll see constantly in Level 2+
problems.
