"""
Problem 4: Search in Rotated Sorted Array

A sorted ascending array of distinct integers has been rotated at some
unknown pivot (e.g. [0,1,2,4,5,6,7] -> [4,5,6,7,0,1,2]). Given the rotated
array `nums` and a `target`, return its index, or -1 if not present.

Example:
    search_rotated([4, 5, 6, 7, 0, 1, 2], 0) -> 4
    search_rotated([4, 5, 6, 7, 0, 1, 2], 3) -> -1
    search_rotated([1], 0) -> -1

Constraints:
    - 1 <= len(nums) <= 5000
    - All elements distinct.
    - Must run in O(log n).

Your task:
    1. The array isn't fully sorted, so you can't directly compare
       `nums[mid]` to `target` and know which half to go to. But one half
       (left of mid, or right of mid) is ALWAYS fully sorted at any given
       `lo`/`hi`/`mid`. Figure out: given `nums[lo]`, `nums[mid]`, how do
       you tell which half is the sorted one?
    2. Once you know which half is sorted, you can check with a normal
       comparison whether `target` could be in that sorted half's range,
       and narrow `lo`/`hi` accordingly.
    3. State final time and space complexity in a comment.
"""


def search_rotated(nums: list[int], target: int) -> int:
    pass


if __name__ == "__main__":
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1
    assert search_rotated([1], 1) == 0
    assert search_rotated([5, 1, 3], 5) == 0
    print("All sample tests passed.")
