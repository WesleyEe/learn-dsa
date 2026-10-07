# Progress Tracker

**Current level:** Level 1 in progress — Unit 1 complete
**Current unit:** Unit 2 — Two Pointers & Sliding Window

## Level 0 — Foundations
- [x] Big-O & complexity analysis (taught in Unit 1 concepts.md)

## Level 1 — Simple screening assessments
- [x] Unit 1 — Complexity, Arrays & Strings
- [ ] Unit 2 — Two Pointers & Sliding Window
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
