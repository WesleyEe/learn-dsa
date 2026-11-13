"""
Problem 3: Find First and Last Position of Element in Sorted Array

Given a sorted (ascending) list of integers `nums` that may contain
duplicates, and an integer `target`, return [first_index, last_index] of
`target`'s occurrences, or [-1, -1] if `target` isn't present.

Example:
    find_first_last([5, 7, 7, 8, 8, 10], 8) -> [3, 4]
    find_first_last([5, 7, 7, 8, 8, 10], 6) -> [-1, -1]
    find_first_last([], 0) -> [-1, -1]

Constraints:
    - 0 <= len(nums) <= 10^5
    - nums is sorted ascending, may contain duplicates.
    - Must run in O(log n) — a linear scan defeats the point of this unit.

Your task:
    1. You need two separate binary searches: one biased to find the
       leftmost occurrence, one biased to find the rightmost. Think about
       what changes in the template when you find a match but want to keep
       searching in a specific direction instead of returning immediately.
    2. Write one helper that takes a "find leftmost" boolean flag, or write
       two near-identical functions — your choice, but don't duplicate the
       whole binary search loop body by copy-paste without understanding
       the one-line difference between the two searches.
    3. State final time and space complexity in a comment.
"""


def find_first_last(nums: list[int], target: int) -> list[int]:
    pass


if __name__ == "__main__":
    assert find_first_last([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert find_first_last([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert find_first_last([], 0) == [-1, -1]
    assert find_first_last([1], 1) == [0, 0]
    assert find_first_last([2, 2, 2, 2], 2) == [0, 3]
    print("All sample tests passed.")
