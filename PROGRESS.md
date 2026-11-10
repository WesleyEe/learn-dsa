# Progress Tracker

**Current level:** Level 1 in progress — Units 1-2 complete
**Current unit:** Unit 3 — Hash Maps & Sets

## Level 0 — Foundations
- [x] Big-O & complexity analysis (taught in Unit 1 concepts.md)

## Level 1 — Simple screening assessments
- [x] Unit 1 — Complexity, Arrays & Strings
- [x] Unit 2 — Two Pointers & Sliding Window
- [ ] Unit 3 — Hash Maps & Sets
- [ ] Unit 4 — Sorting & Binary Search
- [ ] Unit 5 — Basic Recursion
- [ ] **Level 1 review checkpoint**

## Level 2 — Good local company assessments
- [ ] Unit 6 — Linked Lists
- [ ] Unit 7 — Stacks & Queues
- [ ] Unit 8 — Trees & BSTs
- [ ] Unit 9 — Recursion & Backtracking
- [ ] Unit 10 — Sorting Algorithms Deep Dive
- [ ] **Level 2 review checkpoint**

## Level 3 — MNC / mid-tier level
- [ ] Unit 11 — Heaps & Priority Queues
- [ ] Unit 12 — Graphs I (BFS/DFS, Topo Sort)
- [ ] Unit 13 — Union-Find
- [ ] Unit 14 — Dynamic Programming I (1D & 2D)
- [ ] Unit 15 — Tries
- [ ] Unit 16 — Intervals & Greedy
- [ ] Unit 17 — Bit Manipulation
- [ ] **Level 3 review checkpoint**

## Level 4 — FAANG / Meta screening-ready
- [ ] Unit 18 — Advanced DP
- [ ] Unit 19 — Graphs II (Dijkstra, MST)
- [ ] Unit 20 — Advanced Backtracking & Combinatorics
- [ ] Unit 21 — Design Problems (LRU Cache, Iterators, etc.)
- [ ] Unit 22 — String Algorithms (KMP, Rolling Hash)
- [ ] **Level 4 review checkpoint**

## Level 5 — Meta onsite polish
- [ ] Timed mixed mock interviews
- [ ] Verbal-explanation practice
- [ ] **Final certification**

---
*Log notes (dates, weak spots, things to revisit) go below as we go.*

- **2026-10-07 — Unit 1 complete.** All 5 problems solved and verified
  (fuzz-tested, not just sample asserts). Recurring pattern to watch:
  stated complexity not matching actual code — happened 3x (`sum()`
  inside a loop, a dead-but-harmless guard condition, and list slicing
  `nums[1:]` silently costing O(n) space). Build the reflex: check every
  line inside a loop for hidden O(n) work, and treat any `list[a:b]`
  slice as a red flag for "am I copying when I meant to iterate by
  index?" Checkpoint: set-based duplicate detection was clean; binary
  search for insert-position had a real boundary-condition gap (narrowing
  a 2-element range skipped straight past the "length 1" base case to
  empty) — re-anchor on the `lo <= hi` / return `lo` idiom rather than
  "subarray length" reasoning, and always use index pointers (`lo`,
  `hi`) instead of literal slicing for binary search.

- **2026-11-10 — Unit 2 complete.** All 5 problems + 2 checkpoint
  questions solved and fuzz-verified. Recurring bug pattern this unit:
  **state going stale inside a loop** — happened repeatedly: a value
  computed once before a loop but never recomputed after pointers moved
  (review_qn_two's `sum_of_ptr`), a length/window-size computed using a
  pointer *before* it was incremented instead of after (Problem 3's
  first draft), and outer-loop termination relying on a side-effect
  condition that doesn't fire every iteration (Problem 3's infinite
  loop, fixed by switching to `for right in range(n)` instead of a
  `while` keyed off `left`). General lesson: when a loop body recomputes
  something from pointers/indices, double-check it's recomputed in the
  same iteration those pointers changed, not reused from a stale value.
  Also hit two correctness-via-missing-case bugs in Three Sum (duplicate
  triplets from a repeated outer pivot, fixed with the standard
  skip-adjacent-duplicate idiom) — good self-debugging there, correctly
  reasoned that a hand-traced test with no duplicate values could never
  have caught a duplicate-handling bug. Pattern recognition across the
  checkpoint was solid: correctly ruled out sliding window once negative
  values were introduced and reached for prefix-sum+hashmap instead.
