"""
Problem 3: Two Sum

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Assume exactly one valid answer
exists, and you may not use the same element twice. Order of returned
indices doesn't matter.

Example:
    two_sum([2, 7, 11, 15], 9) -> [0, 1]   # 2 + 7 == 9
    two_sum([3, 2, 4], 6) -> [1, 2]        # 2 + 4 == 6
    two_sum([3, 3], 6) -> [0, 1]

Constraints:
    - 2 <= len(nums) <= 10^4

Your task:
    1. Start with the brute-force O(n^2) nested-loop approach.
    2. Then re-read the Unit 1 concepts.md section on dict lookup cost.
       Can you solve this in a single O(n) pass using a dict that maps
       value -> index as you go?
    3. State time and space complexity in a comment.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    # TODO: implement
    pass


if __name__ == "__main__":
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]
    assert sorted(two_sum([3, 3], 6)) == [0, 1]
    print("All sample tests passed.")
