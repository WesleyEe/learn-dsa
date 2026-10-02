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

    def is_alphanumeric(c):
        return c.isascii() and c.isalnum()

    # Handles edge case where s is an empty string
    if len(s) == 0:
        return True

    # Idea here (O(n) time complexity and O(1) space complexity)
    # Have a left pointer that starts from first idx and right pointer from the end idx
    #
    # Loop the below:
    # Left pointer checks if alphanumeric, if no, move one idx down and check again until alphanumeric
    # Right pointer checks if alphanumeric, if no, move one idx up and check again until alphanumeric
    # Once both alphanumeric, compare. If not the same, return False. If the same, begin next loop iteration
    # Once left pointer and right pointer idx meet, or cross each other, break loop and return True

    left_ptr_idx = 0
    right_ptr_idx = len(s) - 1

    while left_ptr_idx < right_ptr_idx:

        while not is_alphanumeric(s[left_ptr_idx]):
            left_ptr_idx += 1
            if left_ptr_idx > right_ptr_idx:
                return True

        while not is_alphanumeric(s[right_ptr_idx]):
            right_ptr_idx -= 1
            if right_ptr_idx < left_ptr_idx:
                return True

        # At this point, both ptr should have an alphanumeric character
        # Else, keep going
        if s[left_ptr_idx].lower() != s[right_ptr_idx].lower():
            return False

        left_ptr_idx += 1
        right_ptr_idx -= 1

    return True


if __name__ == "__main__":
    assert is_palindrome("   ") is True
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("0P") is False
    assert is_palindrome("") is True
    print("All sample tests passed.")
