"""
Problem 1: Binary Search

Given a sorted (ascending) list of distinct integers `nums` and an integer
`target`, return the index of `target` in `nums`, or -1 if it's not present.

Example:
    binary_search([-1, 0, 3, 5, 9, 12], 9) -> 4
    binary_search([-1, 0, 3, 5, 9, 12], 2) -> -1

Constraints:
    - 0 <= len(nums) <= 10^4
    - nums is sorted ascending, all elements distinct.

Your task:
    1. Implement the exact template from concepts.md section 2. Use
       `lo <= hi` as the loop condition, not `lo < hi`.
    2. Make sure it's correct for an empty list and a single-element list.
    3. State final time and space complexity in a comment.
"""


def binary_search(nums: list[int], target: int) -> int:
    pass


if __name__ == "__main__":
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([], 5) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 3) == -1
    print("All sample tests passed.")
