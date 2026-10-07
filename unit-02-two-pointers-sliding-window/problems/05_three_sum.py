"""
Problem 5: Three Sum

Given a list of integers `nums`, return all unique triplets
`[nums[i], nums[j], nums[k]]` (i, j, k all distinct indices) such that
they sum to 0. The returned triplets must not contain duplicate sets of
values, and order within/between triplets doesn't matter.

Example:
    three_sum([-1, 0, 1, 2, -1, -4]) -> [[-1, -1, 2], [-1, 0, 1]]
    three_sum([0, 1, 1]) -> []
    three_sum([0, 0, 0]) -> [[0, 0, 0]]

Constraints:
    - 0 <= len(nums) <= 3000

Your task:
    1. Brute force is O(n^3) — three nested loops. Don't submit that; think
       about how to remove one loop.
    2. Optimal approach: sort `nums` first (O(n log n), and sorting also
       makes duplicate-skipping easy). Then fix one number with an outer
       loop, and use opposite-end two pointers on the *remaining* subarray
       to find pairs that sum to `-nums[i]` — this reuses the exact Shape A
       two-pointer idea from problem 4, nested inside one outer loop.
    3. The tricky part isn't the algorithm, it's avoiding duplicate
       triplets in the output. Since the array is sorted, duplicates sit
       next to each other — after finding a valid triplet, or after trying
       a value for the outer loop, skip forward past any repeated values.
    4. State final time and space complexity in a comment.
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    # TODO: implement
    pass


def _normalize(triplets):
    return sorted(tuple(sorted(t)) for t in triplets)


if __name__ == "__main__":
    assert _normalize(three_sum([-1, 0, 1, 2, -1, -4])) == _normalize(
        [[-1, -1, 2], [-1, 0, 1]]
    )
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([]) == []
    print("All sample tests passed.")
