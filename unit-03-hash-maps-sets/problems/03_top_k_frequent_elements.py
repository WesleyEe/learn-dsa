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

Your task:
    1. Build a frequency count first (collections.Counter is perfect
       here, or a plain dict).
    2. Naive next step: sort the distinct elements by frequency and take
       the top k. What's the complexity of that sort?
    3. You don't actually need a full sort to get the top k — that's
       solving a harder problem than asked (ordering *everything*, when
       you only need the top slice). For this unit, a full sort is an
       acceptable answer (state its complexity honestly). If you want a
       preview of the better approach: a heap can get this to
       O(n log k) instead of O(n log n) — we'll cover heaps properly in
       Unit 11, so don't worry about implementing that now unless you
       want to peek ahead.
    4. State final time and space complexity in a comment for whichever
       approach you actually implement.
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # TODO: implement
    pass


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 4, 1, 1, 1, 2, 2, 2, 2], 2)) == [1, 2]
    print("All sample tests passed.")
