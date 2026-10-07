"""
Problem 3: Minimum Size Subarray Sum

Given an array of positive integers `nums` and a positive integer `target`,
return the length of the shortest contiguous subarray whose sum is >=
`target`. If no such subarray exists, return 0.

Example:
    min_subarray_len([2, 3, 1, 2, 4, 3], 7) -> 2
    # subarray [4, 3] has sum 7, length 2 (shortest possible)

    min_subarray_len([1, 1, 1, 1, 1], 11) -> 0
    # no subarray sums to >= 11

    min_subarray_len([1, 4, 4], 4) -> 1

Constraints:
    - 1 <= len(nums) <= 10^5
    - 1 <= nums[i] <= 10^4
    - 1 <= target <= 10^9

Your task:
    1. Note all values are positive — that matters. It means growing the
       window always increases the sum, and shrinking it always decreases
       the sum, so there's no ambiguity about which direction fixes a
       "too big" or "too small" window.
    2. Same variable-window template as problem 2, but now the condition
       for shrinking is about the running sum vs target, not duplicates.
       Here you shrink *while the window is already valid* (sum >= target)
       to find the minimum — the opposite trigger from problem 2, where you
       shrunk while the window was *invalid*. Make sure you understand why
       the two problems shrink on opposite conditions before coding this.
    3. State final time and space complexity in a comment.
"""


def min_subarray_len(nums: list[int], target: int) -> int:
    # TODO: implement
    pass


if __name__ == "__main__":
    assert min_subarray_len([2, 3, 1, 2, 4, 3], 7) == 2
    assert min_subarray_len([1, 1, 1, 1, 1], 11) == 0
    assert min_subarray_len([1, 4, 4], 4) == 1
    assert min_subarray_len([1, 1, 1, 1, 1, 1, 1, 1], 4) == 4
    print("All sample tests passed.")
