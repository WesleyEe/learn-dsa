"""
Problem 2: Valid Palindrome (alphanumeric only, case-insensitive)

Given a string `s`, return True if it reads the same forward and backward,
considering only alphanumeric characters and ignoring case.

Example:
    is_palindrome("A man, a plan, a canal: Panama") -> True
    is_palindrome("race a car") -> False
    is_palindrome(" ") -> True   # empty after filtering counts as palindrome

Constraints:
    - 0 <= len(s) <= 2 * 10^5

Your task:
    1. Do NOT build a cleaned copy of the string and then compare it to its
       reverse using two full extra string copies if you can avoid it —
       think about whether you actually need one, and whether two pointers
       (one from each end) can solve this in O(1) extra space (ignoring the
       input itself).
    2. State time and space complexity in a comment.
"""


def is_palindrome(s: str) -> bool:
    # TODO: implement
    pass


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("0P") is False
    assert is_palindrome("") is True
    print("All sample tests passed.")
