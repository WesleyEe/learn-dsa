"""
Problem 2: Search Insert Position

Given a sorted (ascending) list of distinct integers `nums` and an integer
`target`, return the index where `target` is found, or the index where it
would be inserted to keep `nums` sorted if it's not present.

Example:
    search_insert([1, 3, 5, 6], 5) -> 2
    search_insert([1, 3, 5, 6], 2) -> 1
    search_insert([1, 3, 5, 6], 7) -> 4
    search_insert([1, 3, 5, 6], 0) -> 0

Constraints:
    - 0 <= len(nums) <= 10^4
    - nums is sorted ascending, all elements distinct.

Your task:
    1. This is the same template as Problem 1 — the only change is what you
       return when the loop exits without finding an exact match. Recall
       from concepts.md: `lo` converges to the correct insertion point.
    2. Don't special-case "not found" separately from "found" — one return
       value at the end should cover both, if you set it up right.
    3. State final time and space complexity in a comment.
"""


def search_insert(nums: list[int], target: int) -> int:
    pass


if __name__ == "__main__":
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    assert search_insert([], 5) == 0
    print("All sample tests passed.")
