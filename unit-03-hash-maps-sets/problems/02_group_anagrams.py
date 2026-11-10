"""
Problem 2: Group Anagrams

Given a list of strings `strs`, group the anagrams together. Return a list
of groups (each group is a list of strings); groups and the strings within
them can be in any order.

Example:
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    group_anagrams([""]) -> [[""]]
    group_anagrams(["a"]) -> [["a"]]

Constraints:
    - 0 <= len(strs) <= 10^4
    - Lowercase English letters only.

Your task:
    1. For each string, compute a "canonical key" that is identical for
       every anagram of the same letters and different otherwise (see
       concepts.md section 3 for the hint).
    2. Use a dict mapping that key -> list of original strings
       (collections.defaultdict(list) removes the need to check if the
       key already exists before appending).
    3. State final time and space complexity in a comment. (Think about
       the cost of computing the canonical key for a string of length k —
       it's not free, and it happens once per string.)
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    # TODO: implement
    pass


def _normalize(groups):
    return sorted(tuple(sorted(g)) for g in groups)


if __name__ == "__main__":
    assert _normalize(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == _normalize(
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    )
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams([]) == []
    print("All sample tests passed.")
