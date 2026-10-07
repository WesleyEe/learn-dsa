"""
Problem 1: Maximum Sum Subarray of Fixed Size K

Given a list of integers `nums` and an integer `k`, return the maximum sum
of any contiguous subarray of exactly length `k`.

Example:
    max_sum_fixed_window([2, 1, 5, 1, 3, 2], 3) -> 9
    # subarray [5, 1, 3] has sum 9

    max_sum_fixed_window([2, 3, 4, 1, 5], 2) -> 7
    # subarray [3, 4] has sum 7

Constraints:
    - 1 <= k <= len(nums) <= 10^5

Your task:
    1. Brute force: for every starting index, sum the next k elements.
       What's the complexity? (hint: it's not O(n), think about what
       "sum the next k elements" costs if you recompute it every time)
    2. Optimal: use a fixed-size sliding window. As the window slides one
       step right, you only need to add the new element entering and
       subtract the element leaving — don't recompute the sum from scratch.
    3. State final time and space complexity in a comment.
"""


def max_sum_fixed_window(nums: list[int], k: int) -> int:
    # TODO: implement
    pass


if __name__ == "__main__":
    assert max_sum_fixed_window([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_fixed_window([2, 3, 4, 1, 5], 2) == 7
    assert max_sum_fixed_window([5], 1) == 5
    assert max_sum_fixed_window([1, 1, 1, 1], 4) == 4
    print("All sample tests passed.")
