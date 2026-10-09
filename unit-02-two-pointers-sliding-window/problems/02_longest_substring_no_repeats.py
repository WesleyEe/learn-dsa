"""
Problem 2: Longest Substring Without Repeating Characters

Given a string `s`, return the length of the longest substring that has no
repeating characters.

Example:
    longest_substring_no_repeats("abcabcbb") -> 3   # "abc"
    longest_substring_no_repeats("bbbbb") -> 1       # "b"
    longest_substring_no_repeats("pwwkew") -> 3      # "wke"
    longest_substring_no_repeats("") -> 0

Constraints:
    - 0 <= len(s) <= 5 * 10^4

Your task:
    1. This is a variable-size sliding window. Grow the window by moving
       `right` forward, tracking which characters are currently inside it
       (a set, or a dict mapping char -> its most recent index both work —
       try the set version first, it's simpler to reason about).
    2. When you encounter a character already in the window, you must
       shrink from the left until the duplicate is gone — remember `left`
       only ever moves forward, never resets to 0.
    3. State final time and space complexity in a comment. (Space here
       depends on the character set size, not just n — think about why.)
"""


def longest_substring_no_repeats(s: str) -> int:
    # The time complexity is O(n) while space complexity is O(1)
    if len(s) == 0:
        return 0

    longest_len = 1
    curr_len = 1
    right_ptr_idx = 1
    left_ptr_idx = 0
    seen_chars = {s[left_ptr_idx]}

    # will run if len(s) is 2 or greater, else will skip this block
    while right_ptr_idx < len(s):
        if s[right_ptr_idx] not in seen_chars:
            seen_chars.add(s[right_ptr_idx])
            curr_len += 1
            if curr_len > longest_len:
                longest_len = curr_len
        else:
            # repeating char
            dup_char = s[right_ptr_idx]
            while s[left_ptr_idx] != dup_char:
                seen_chars.remove(s[left_ptr_idx])
                left_ptr_idx += 1
            curr_len = right_ptr_idx - left_ptr_idx
            left_ptr_idx += 1
        right_ptr_idx += 1

    return longest_len


if __name__ == "__main__":
    assert longest_substring_no_repeats("abca") == 3
    assert longest_substring_no_repeats("abcabcbb") == 3
    assert longest_substring_no_repeats("bbbbb") == 1
    assert longest_substring_no_repeats("pwwkew") == 3
    assert longest_substring_no_repeats("") == 0
    assert longest_substring_no_repeats("abba") == 2
    print("All sample tests passed.")
