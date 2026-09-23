# Learn DS&A — Zero to Meta-Ready

A structured, project-based path from "rusty, informal DS&A knowledge" to
"ready for Meta-level onsite technical screens." Language: **Python 3**.

## How this works

1. Each **unit** lives in its own folder (`unit-01-...`, `unit-02-...`, etc.).
2. Every unit has:
   - `concepts.md` — the teaching material for that unit. Read this first.
   - `problems/` — starter files, one per problem. Each has a function
     signature, a docstring with the task + examples, and a
     `if __name__ == "__main__":` block with sample test cases you can run.
   - `README.md` — the unit's checklist and instructions.
3. You solve the problems by editing the starter files directly.
4. When you're done with a unit (or want a check-in), tell me and paste your
   code or just say "review unit 3." I will:
   - Grade correctness, complexity, and code quality
   - Fix/explain any bugs and explain *why* the fix works
   - Point out the idiomatic/optimal approach if yours wasn't
   - Write a short summary of what you now know solidly vs. what's shaky
5. At the end of each unit there's a **review checkpoint** — a few mixed
   problems pulling from everything so far, to make sure it stuck.
6. Only new units are scaffolded as you reach them — I'll create unit
   folders on demand so we're not staring at 15 empty folders on day one.
   `PROGRESS.md` tracks where you are.

Run any file directly to sanity-check against the built-in sample cases:

```bash
python3 unit-01-complexity-arrays-strings/problems/01_two_sum.py
```

I'll also give you extra hidden-edge-case tests during review, not just what's
in the starter file — the starter file's cases are a smoke test, not full
coverage. That mirrors real OAs, where the visible examples are never the
whole test suite.

## The leveling system

Progress is milestone-based, not time-based. After each level's units are
reviewed and you're solving that tier's problems in roughly 20-35 minutes
each without hints, I'll certify you at that level and tell you explicitly.
Here's the full ladder:

### Level 0 — Foundations
**Unlocks:** understanding *why* any of this matters.
Big-O analysis, how to reason about time/space complexity, Python's
built-in data structures and their real costs (list vs. set vs. dict vs.
deque), how to talk through a problem out loud.

### Level 1 — "Ready for simple screening assessments"
*(basic HackerRank-style OAs, early-stage startups, bootcamp-grad bar)*
Arrays & strings, two pointers, sliding window (basic), hash maps/sets,
basic sorting & binary search, basic recursion.

### Level 2 — "Ready for good local company assessments"
*(solid regional tech companies, most non-FAANG product companies)*
Linked lists, stacks & queues, trees (BST + traversals), recursion &
backtracking fundamentals, sorting algorithms in depth, two
pointers/sliding window (advanced).

### Level 3 — "MNC / mid-tier tech company level"
*(larger multinational tech companies, solid mid-size product companies)*
Heaps/priority queues, graphs (BFS/DFS, topological sort, union-find),
dynamic programming (1D & 2D), tries, intervals & greedy algorithms, bit
manipulation.

### Level 4 — "FAANG / Meta screening-ready"
*(what actually shows up in Meta phone screens and onsites)*
Advanced DP (knapsack variants, DP on trees/grids, state compression),
advanced graphs (Dijkstra, MST, advanced union-find), advanced
backtracking & combinatorics, design-lite problems (LRU cache, iterator
design), hard string algorithms (KMP/rolling hash), optimizing brute
force → optimal under time pressure.

### Level 5 — "Meta onsite polish"
Timed mixed mock interviews across all topics, explaining your approach
out loud before coding (this is graded at Meta), handling follow-up
"now optimize further" pressure, recognizing problem patterns fast,
common Meta-tagged question styles.

At the start of each level I'll teach any new prerequisite concepts before
handing you problems — you won't be asked to use a tool you haven't been
taught yet.

## Current status

See `PROGRESS.md`.
