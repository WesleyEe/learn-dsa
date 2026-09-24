"""
Problem 1: Maximum Subarray Sum

Given a list of integers `nums` (may include negative numbers), return the
largest possible sum of a *contiguous* subarray.

Example:
    max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6
    # the subarray [4, -1, 2, 1] has the largest sum, 6

    max_subarray_sum([1]) -> 1
    max_subarray_sum([-1, -2, -3]) -> -1   # must pick at least one element

Constraints:
    - 1 <= len(nums) <= 10^5
    - The array always has at least one element.

Your task:
    1. First write the brute-force O(n^2) version (check every subarray)
       and state its complexity in a comment.
    2. Then think about whether you can do it in a single O(n) pass.
       Hint: at each position, ask "is it better to extend the previous
       subarray, or start fresh from here?"
    3. State the final time and space complexity in a comment above your
       function.
"""

# # The below solution has time complexity of O(n^2), as it relies on brute-force and has a nested for loop. 
# # The space complexity is O(1).
# def max_subarray_sum(nums: list[int]) -> int:

#     max_sum = float('-inf')
#     for idx in range(len(nums)): 

#         curr_sum = nums[idx]

#         if curr_sum > max_sum: 
#             max_sum = curr_sum

#         for idx2 in range(idx + 1, len(nums)):
#             curr_sum += nums[idx2]

#             if curr_sum > max_sum:
#                 max_sum = curr_sum

#     return max_sum

# The optimal solution below has time complexity of O(n), and the space complexity is O(1).
def max_subarray_sum(nums: list[int]) -> int:
    """Kadane's algorithm"""
    best_ending_here = nums[0]
    best_overall = nums[0]
    for idx in range(1, len(nums)):
        best_ending_here = max(nums[idx], best_ending_here + nums[idx])
        best_overall = max(best_overall, best_ending_here)
    return best_overall


if __name__ == "__main__":
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([1]) == 1
    assert max_subarray_sum([-1, -2, -3]) == -1
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23
    print("All sample tests passed.")
