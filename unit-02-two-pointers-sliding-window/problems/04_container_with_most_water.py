"""
Problem 4: Container With Most Water

You're given a list of non-negative integers `heights`, where `heights[i]`
is the height of a vertical line at position `i`. Choose two lines that,
together with the x-axis, form a container. Return the maximum amount of
water it can hold.

The container's capacity is `(right_index - left_index) * min(heights[left], heights[right])`
— the width times the shorter of the two walls (water spills over the
shorter wall).

Example:
    max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) -> 49
    # lines at index 1 (height 8) and index 8 (height 7): width 7, height 7 -> 49

    max_area([1, 1]) -> 1

Constraints:
    - 2 <= len(heights) <= 10^5

Your task:
    1. Brute force: check every pair of lines. What's the complexity?
    2. Optimal: this is opposite-end two pointers (Shape A from
       concepts.md), NOT a sliding window — there's no "window sum" to
       maintain. Start with the widest possible container (both pointers
       at the ends) and think about which pointer it's ever beneficial to
       move inward. Hint: if `heights[left] < heights[right]`, is there
       any reason to move `right` inward instead of `left`? Think about
       what moving the taller pointer inward could possibly gain you,
       given that width can only decrease from here.
    3. State final time and space complexity in a comment.
"""


def max_area(heights: list[int]) -> int:
    # TODO: implement
    pass


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    print("All sample tests passed.")
