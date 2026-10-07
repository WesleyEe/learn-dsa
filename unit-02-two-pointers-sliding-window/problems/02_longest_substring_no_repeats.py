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
    # TODO: implement
    pass


if __name__ == "__main__":
    assert longest_substring_no_repeats("abcabcbb") == 3
    assert longest_substring_no_repeats("bbbbb") == 1
    assert longest_substring_no_repeats("pwwkew") == 3
    assert longest_substring_no_repeats("") == 0
    assert longest_substring_no_repeats("abba") == 2
    print("All sample tests passed.")
