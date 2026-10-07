"""
Problem 5: Remove Duplicates from Sorted Array

Given a sorted (ascending) list of integers `nums` (may contain duplicates),
remove the duplicates in-place so each unique element appears only once.
Return the number of unique elements, `k`. The first `k` elements of `nums`
must hold the unique elements in their original order; what's after index
`k-1` doesn't matter.

Example:
    nums = [1, 1, 2]
    k = remove_duplicates(nums)
    # k == 2, and nums[:k] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    # k == 5, and nums[:k] == [0, 1, 2, 3, 4]

Constraints:
    - 1 <= len(nums) <= 3 * 10^4
    - nums is sorted in non-decreasing order.
    - Must be O(1) extra space (in-place, no copying to a new list/set).

Your task:
    1. Because the array is sorted, duplicates are always adjacent — you
       don't need a set to detect them.
    2. Same slow/fast pointer idea as problem 4.
    3. State time and space complexity in a comment.
"""


def remove_duplicates(nums: list[int]) -> int:
    # The time complexity of this soln is O(n) and space complexity is O(1)
    curr_num = nums[0]
    position_idx = 1
    unique_items = 1

    for idx in range(1, len(nums)):
        num = nums[idx]
        if num != curr_num:
            nums[position_idx] = num
            position_idx += 1
            unique_items += 1
            curr_num = num

    return unique_items


if __name__ == "__main__":
    nums = [1, 1, 2]
    k = remove_duplicates(nums)
    assert k == 2 and nums[:k] == [1, 2], (k, nums)

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = remove_duplicates(nums2)
    assert k2 == 5 and nums2[:k2] == [0, 1, 2, 3, 4], (k2, nums2)

    nums3 = [1]
    k3 = remove_duplicates(nums3)
    assert k3 == 1 and nums3[:k3] == [1], (k3, nums3)

    nums4 = [1, 2, 2, 2, 3, 3, 4]
    k4 = remove_duplicates(nums4)
    assert k4 == 4 and nums4[:k4] == [1, 2, 3, 4], (k2, nums4)

    print("All sample tests passed.")
