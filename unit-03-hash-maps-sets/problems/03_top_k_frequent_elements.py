"""
Problem 3: Top K Frequent Elements

Given a list of integers `nums` and an integer `k`, return the `k` most
frequent elements. Any order is fine; it's guaranteed the answer is
unambiguous (no ties at the cutoff that would make the answer ambiguous).

Example:
    top_k_frequent([1, 1, 1, 2, 2, 3], 2) -> [1, 2]
    top_k_frequent([1], 1) -> [1]
    top_k_frequent([4, 4, 1, 1, 1, 2, 2, 2, 2], 2) -> [2, 1]

Constraints:
    - 1 <= len(nums) <= 10^5
    - 1 <= k <= number of distinct elements in nums

"""

import heapq
from collections import Counter


# Time complexity is O(n + d log k) and space complexity is O(d + k)
def top_k_frequent(nums: list[int], k: int) -> list[int]:

    dict_counter = Counter(nums)

    return heapq.nlargest(k, dict_counter, key=dict_counter.get)


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 4, 1, 1, 1, 2, 2, 2, 2], 2)) == [1, 2]
    print("All sample tests passed.")
