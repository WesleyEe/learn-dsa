"""
Problem 5: Contains Duplicate Within Distance K

Given a list of integers `nums` and an integer `k`, return True if there
are two distinct indices `i` and `j` such that `nums[i] == nums[j]` and
the absolute difference between `i` and `j` is at most `k`.

Example:
    contains_nearby_duplicate([1, 2, 3, 1], 3) -> True
    # indices 0 and 3 both hold 1, |0-3| = 3 <= 3

    contains_nearby_duplicate([1, 0, 1, 1], 1) -> True
    # indices 2 and 3 both hold 1, |2-3| = 1 <= 1

    contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2) -> False
    # the two 1's are 3 apart, too far for k=2

Constraints:
    - 1 <= len(nums) <= 10^5
    - 0 <= k <= len(nums)

Your task:
    1. This is a direct extension of Unit 1's Two Sum dict-of-index idea:
       track the most recent index each value was seen at.
    2. As you scan, for each value check: have I seen this value before,
       and if so, is the distance to that previous index <= k? If yes,
       return True immediately.
    3. Think about whether you need to keep every past index for a value,
       or just the most recent one. (Hint: if the most recent occurrence
       is too far away, could an even older one possibly be closer?)
    4. State final time and space complexity in a comment.
"""


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    # TODO: implement
    pass


if __name__ == "__main__":
    assert contains_nearby_duplicate([1, 2, 3, 1], 3) is True
    assert contains_nearby_duplicate([1, 0, 1, 1], 1) is True
    assert contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2) is False
    assert contains_nearby_duplicate([1], 0) is False
    print("All sample tests passed.")
