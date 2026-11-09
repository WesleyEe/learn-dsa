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

    # The idea here: Outer loop with closing window on remaining subarray
    # If nums has len < 3, immediately return empty list
    # Else, first sort the nums array in ascending order
    # Fix the first num as the outer number, and do a closing window on the remaining subarr, trying to find a pair that equals to negative of outer number
    # If such a pair is found, record and skip all duplicate values in that subarr
    # After scanning the subarr, skip any duplicate outer number and move to the next non-duplicate outer number. Repeat scanning the new remaining subarr.
    # End when the outer number is the 2nd last number of the array

    triplets_sum_zero = []

    if len(nums) < 3:
        return triplets_sum_zero

    sorted_nums = sorted(nums)

    for idx in range(len(sorted_nums) - 2):

        if idx > 0 and sorted_nums[idx] == sorted_nums[idx - 1]:
            continue

        outer_num = sorted_nums[idx]
        window_left_idx = idx + 1
        window_right_idx = len(sorted_nums) - 1

        while window_left_idx < window_right_idx:
            curr_left_value = sorted_nums[window_left_idx]
            curr_right_value = sorted_nums[window_right_idx]

            window_sum = curr_left_value + curr_right_value

            if window_sum > -outer_num:
                window_right_idx -= 1
            elif window_sum < -outer_num:
                window_left_idx += 1
            # Once found the triplet that sums to zero
            else:
                triplets_sum_zero.append([outer_num, curr_left_value, curr_right_value])

                while window_left_idx < window_right_idx:
                    window_left_idx += 1
                    window_right_idx -= 1

                    if sorted_nums[window_left_idx] != curr_left_value:
                        break
                    if sorted_nums[window_right_idx] != curr_right_value:
                        break

    return triplets_sum_zero


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
