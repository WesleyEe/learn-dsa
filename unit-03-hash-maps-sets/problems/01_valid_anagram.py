"""
Problem 1: Valid Anagram

Given two strings `s` and `t`, return True if `t` is an anagram of `s`
(same characters, same counts, any order).

Example:
    is_anagram("anagram", "nagaram") -> True
    is_anagram("rat", "car") -> False
    is_anagram("aacc", "ccac") -> False

Constraints:
    - 0 <= len(s), len(t) <= 5 * 10^4
    - Lowercase English letters only.

Your task:
    1. Brute force: sort both strings and compare. What's the complexity?
       (This is a legitimate, commonly-accepted solution, not a bad one —
       but there's a way to avoid the sort entirely.)
    2. Optimal: use frequency counting instead of sorting. Build a count
       of characters in `s`, then walk through `t` decrementing counts
       (or build two separate frequency dicts/Counters and compare them).
       Think about what must be true at the end if they're anagrams: every
       count should land back at exactly zero, and lengths must match
       first (free early exit).
    3. State final time and space complexity in a comment. (Space here:
       same consideration as Unit 2's character-set question — is it
       bounded by alphabet size or not?)
"""


def is_anagram(s: str, t: str) -> bool:
    # TODO: implement
    pass


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("aacc", "ccac") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "ab") is False
    print("All sample tests passed.")
