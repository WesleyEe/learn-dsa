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

    # The idea here
    # Avoid expensive operations on the array such as insert, use update instead

    # Init a zero counter var, and a postition ptr at idx 0
    # Iterate down the array
    # For each zero value, increase the zero counter and DO NOT move the position ptr down
    # For each non-zero value, update the position ptr idx with that value and move position ptr down by one
    # Update the last idxs of the array with the num of zeros in the zero counter (if there is at least 1 zero)

    # The time complexity of this soln is O(n) and the space complexity is O(1)

    zero_counter = 0
    position_ptr_idx = 0

    for num in nums:
        if num == 0:
            zero_counter += 1
        else:
            nums[position_ptr_idx] = num
            position_ptr_idx += 1

    if zero_counter > 0:
        nums[-zero_counter:] = zero_counter * [0]

    return


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

    nums4 = [1, 3, 2, 0, 0]
    move_zeroes(nums4)
    assert nums4 == [1, 3, 2, 0, 0], nums4

    nums5 = [1, 3, 2, 0, 0, 7]
    move_zeroes(nums5)
    assert nums5 == [1, 3, 2, 7, 0, 0], nums5

    print("All sample tests passed.")
