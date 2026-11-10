"""
Problem 4: Longest Consecutive Sequence

Given an unsorted list of integers `nums`, return the length of the
longest run of consecutive integers (they don't need to be adjacent in
the array, just present in the array as a set of values).

Example:
    longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
    # the longest run is 1, 2, 3, 4

    longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) -> 9
    # 0 through 8

Constraints:
    - 0 <= len(nums) <= 10^5

Your task:
    1. The obvious approach is: sort, then scan for consecutive runs.
       That's O(n log n). This problem specifically wants O(n) — the
       sort is the bottleneck you need to remove.
    2. Put all values in a set for O(1) membership checks (see concepts.md
       section 4 — this is exactly that substitution: you don't need
       sorted order, you need fast "is this value present" checks).
    3. The key trick: only start counting a sequence from a number that
       is the *start* of a sequence — i.e., `num - 1` is NOT in the set.
       For every other number, skip it (it'll get counted when you reach
       its sequence's actual start). Without this check, you'd re-walk
       the same sequence from every one of its members, costing O(n) per
       number instead of O(n) total.
    4. State final time and space complexity in a comment.
"""


def longest_consecutive(nums: list[int]) -> int:
    # TODO: implement
    pass


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1, 2, 0, 1]) == 3
    print("All sample tests passed.")
