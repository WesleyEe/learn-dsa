"""
Problem 4: Move Zeroes

Given a list of integers `nums`, move all 0's to the end while maintaining
the relative order of the non-zero elements. Must be done **in-place**
(modify `nums` directly) without making a copy of the array.

Example:
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    # nums is now [1, 3, 12, 0, 0]

Constraints:
    - 1 <= len(nums) <= 10^4
    - Must operate in-place: O(1) extra space (not counting the input list).

Your task:
    1. This function returns nothing (None) — it mutates `nums` directly,
       like Python's own list.sort().
    2. Think about a "slow pointer" that tracks where the next non-zero
       value should go, while a "fast pointer" scans the array.
    3. State time and space complexity in a comment.
"""


def move_zeroes(nums: list[int]) -> None:
    # TODO: implement (mutate nums in place, do not return anything)
    pass


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums == [1, 3, 12, 0, 0], nums

    nums2 = [0, 0, 1]
    move_zeroes(nums2)
    assert nums2 == [1, 0, 0], nums2

    nums3 = [1, 2, 3]
    move_zeroes(nums3)
    assert nums3 == [1, 2, 3], nums3

    print("All sample tests passed.")
