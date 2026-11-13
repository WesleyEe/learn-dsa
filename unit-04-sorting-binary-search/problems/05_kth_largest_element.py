"""
Problem 5: Kth Largest Element in an Array

Given a list of integers `nums` and an integer `k`, return the kth largest
element (1st largest = the max, not the kth distinct value — duplicates
count individually).

Example:
    find_kth_largest([3, 2, 1, 5, 6, 4], 2) -> 5
    find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) -> 4

Constraints:
    - 1 <= len(nums) <= 10^5
    - 1 <= k <= len(nums)

Your task:
    1. Simplest correct approach: sort and index. State its complexity —
       is it the best you can do?
    2. Better: this is exactly Unit 3's Top-K pattern in disguise. You
       already know how to get the k largest via a size-k heap — adapt
       that (hint: `heapq` has a direct one-liner for "kth largest" too,
       similar to `nlargest`).
    3. (Stretch, optional) Quickselect: partition-based selection, average
       O(n). Only attempt this after the heap version is solid — ask me
       for a walkthrough if you want to try it.
    4. State final time and space complexity in a comment for whichever
       approach you submit.
"""


def find_kth_largest(nums: list[int], k: int) -> int:
    pass


if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1
    assert find_kth_largest([2, 1], 2) == 1
    print("All sample tests passed.")
