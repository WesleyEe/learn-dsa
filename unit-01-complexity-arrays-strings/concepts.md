# Unit 1 — Complexity Analysis, Arrays & Strings

Read this whole thing before opening the problems folder. This is the only
unit where the concepts section is long — future units assume you have this
down and just add on top of it.

## 1. Why Big-O is the whole game

An interviewer almost never cares whether your code "works" in isolation —
they care whether you can identify the cost of your approach and whether a
cheaper one exists. Big-O describes how the *runtime* or *memory* of your
solution grows as input size `n` grows, ignoring constant factors.

Common orders, cheapest to most expensive:
```
O(1)        constant       — dict lookup, array index access
O(log n)    logarithmic    — binary search
O(n)        linear         — single pass over a list
O(n log n)  linearithmic   — efficient sorting (merge/quick/heap sort)
O(n^2)      quadratic      — nested loop over the same input
O(2^n)      exponential    — brute-force subsets/combinations
O(n!)       factorial      — brute-force permutations
```

**How to compute it yourself:** count how the number of operations scales
with `n`, drop constants and lower-order terms. `3n + 100` is O(n). A loop
inside a loop, both over `n`, is O(n²) — *unless* the inner loop's range
shrinks or is bounded by a constant, in which case look closer.

**Space complexity** works the same way but counts extra memory you
allocate — not counting the input itself unless you copy it. A hash map that
grows with input is O(n) space. Recursion also costs space: each call frame
sits on the call stack, so a recursion `n` deep costs O(n) space even if you
allocate nothing else.

**Rule of thumb for interviews:** always state your solution's time and
space complexity out loud/in comments before or after you write it, even if
not asked. This is graded even when unstated as a requirement.

## 2. Python data structure costs (memorize this table)

This is the single highest-leverage table in this whole course. Most
"optimize your solution" moments in interviews are just "you used the wrong
data structure."

| Structure | Access | Search | Insert (end) | Insert (arbitrary) | Delete (end) | Delete (arbitrary) |
|---|---|---|---|---|---|---|
| `list` | O(1) | O(n) | O(1) amortized | O(n) | O(1) | O(n) |
| `dict` / `set` | — | O(1) avg | O(1) avg | O(1) avg | — | O(1) avg |
| `collections.deque` | O(n) middle, O(1) ends | O(n) | O(1) both ends | O(n) | O(1) both ends | O(n) |

Key takeaways:
- `x in my_list` is O(n). `x in my_set` / `x in my_dict` is O(1) average.
  **This single fact is behind half of all "optimize this" interview
  follow-ups** — swapping a list membership check for a set turns O(n²)
  into O(n).
- Python lists are dynamic arrays, not linked lists — indexing is O(1),
  but inserting/removing from the *front* is O(n) because everything shifts.
  Use `collections.deque` if you need fast operations at both ends.
- Strings in Python are immutable — every concatenation (`s += char`)
  creates a new string, so building a string in a loop via `+=` is O(n²)
  overall. Use a list and `''.join(list)` at the end instead (O(n)).

## 3. The two-pointer and sliding-window *preview*

You'll learn these properly in Unit 2, but you'll bump into the *pattern*
in this unit's problems, so here's the one-line version: when a problem
involves a contiguous run of an array/string, or comparing elements from
both ends, ask "can I use two pointers instead of nested loops?" before
reaching for brute force.

## 4. How to approach any problem (use this process every time)

1. **Restate the problem** in your own words. Confirm input format, edge
   cases (empty input? duplicates? negative numbers?).
2. **Say the brute-force approach out loud**, with its complexity — even if
   you already see the better one. It anchors the conversation and often
   *is* good enough for easy problems.
3. **Ask "what's the bottleneck?"** — usually a nested loop or repeated
   search. Then ask which data structure removes it.
4. **Code it.** Narrate as you go.
5. **Trace through one example by hand** before declaring done.
6. **State final time/space complexity.**

Use this process on every problem below, even though no one's watching —
building the habit now is the point.

## What you'll practice in this unit

Straight array/string manipulation problems where the *only* skill being
tested is: did you pick an O(n) or O(n log n) approach instead of an O(n²)
one, and did you handle edge cases (empty input, single element, all
duplicates). No pointers/windows/hashing tricks required yet (though you're
free to notice and use them) — that's next unit.
