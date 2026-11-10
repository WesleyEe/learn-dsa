# Unit 3 — Hash Maps & Sets

You've been using dicts and sets informally since Unit 1 (Two Sum, the
sliding-window character set). This unit formalizes *why* they're so
powerful, introduces the Python tools that make them less tedious to use
correctly, and covers the handful of problem shapes that are "just
hashing" once you see them.

## 1. Why hashing is O(1) (a one-level-deeper look)

A hash map stores entries in buckets determined by `hash(key)`. Looking
up a key computes its hash, jumps straight to that bucket, and (assuming
few collisions) finds the value immediately — no scanning. This is why
`dict`/`set` operations are O(1) *average case*, regardless of how many
entries exist. The "average case" caveat matters: worst case is O(n) if
many keys collide into the same bucket, but Python's hash function is
good enough that you can treat O(1) as the practical reality for
interview purposes. You don't need to implement hashing yourself — just
know *why* the O(1) claim holds, since interviewers sometimes ask.

**Hashability requirement:** only immutable types can be dict keys / set
members — `int`, `str`, `tuple`, `frozenset`. Lists and dicts can't be
keys (you hit this in the Three Sum discussion — you'd need `tuple(x)` to
put a list's contents into a set). This is a direct consequence of how
hashing works: if a key's contents (and thus its hash) could change after
insertion, the map couldn't reliably find it again.

## 2. Three use-cases that cover 90% of hashing problems

**(a) Existence / membership check.** "Have I seen this before?" →
`set()`. You used this for the sliding-window duplicate check and the
`set(nums)` discussion for duplicate detection. O(1) lookup replaces an
O(n) list scan.

**(b) Frequency counting.** "How many times does each thing appear?" →
`dict` mapping value → count, or Python's `collections.Counter` (a dict
subclass purpose-built for this — `Counter(some_list)` builds the whole
frequency map in one call, and supports `.most_common(k)`).

**(c) Grouping / bucketing.** "Put these items into groups by some key."
→ `dict` mapping group-key → list of items, using
`collections.defaultdict(list)` so you don't need an `if key not in
dict: dict[key] = []` check before every append — `defaultdict` creates
the empty value automatically the first time a new key is touched.

```python
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[some_key_function(item)].append(item)
```

This removes an entire category of bugs you've hit twice already this
course (checking the wrong thing before deciding whether to initialize
vs. update a dict entry) by making "does this key already exist" a
non-issue.

## 3. Picking the right key for grouping problems

For grouping problems (e.g., "group these strings if they're anagrams of
each other"), the hard part is rarely the data structure — it's figuring
out *what key* maps all members of a group to the same value. For
anagrams specifically: two strings are anagrams iff sorting their
characters produces the same string, so `''.join(sorted(s))` is a key
that's identical for every anagram of the same letters, and different
otherwise. This "find the canonical/normalized form" trick — reduce each
item to some representative value, then group by that — is reusable far
beyond anagrams.

## 4. Hash sets for O(n) problems that look like they need sorting

Some problems look like they need the array sorted (e.g., "find the
longest run of consecutive integers"), but sorting costs O(n log n). If
all you actually need is O(1) "is this value present" checks — not the
values in sorted *order* — a hash set gets you there in O(n). Watch for
this substitution opportunity: "I think I need this sorted" is often
really "I think I need fast membership checks," and those aren't the
same requirement.

## What you'll practice in this unit

Frequency comparison, grouping by a normalized key, top-k by frequency,
a hash-set trick that beats sorting, and a bounded-distance duplicate
check that revisits the "track most recent index" idea from Unit 1's Two
Sum but with an added constraint.
