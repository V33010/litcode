"""
LeetCode 0003: longest substring without repeats
Difficulty: Medium
"""


def check_valid(s: str) -> bool:
    print(f"testing: {s}")
    is_valid = True
    current = ""
    while len(s) > 1:
        current = s[0]
        s = s[1:]
        if current in s:
            is_valid = False
            return is_valid

    return is_valid


def window_slice(window_size, s: str):
    i_max = len(s) - window_size + 1
    print(f"i_max: {i_max}")
    for i in range(i_max):
        string_slice = s[i : i + window_size]
        if check_valid(string_slice):
            return True

    return False


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = len(s)
        if window == 1:
            print("from if window == 1: answer: 1")
            return 1

        if window == 2:
            if s[0] != s[1]:
                print("from if window == 2, answer: 2")
                return 2
            print("from if window == 2, answer: 1")
            return 1

        while window > 0:
            print(f"testing window size: {window}")
            if window_slice(window, s):
                print(window)
                return window
            window -= 1

        print(0)

        return 0


if __name__ == "__main__":
    sol = Solution()

    # -------- Test Cases --------

    # Basic cases
    assert sol.lengthOfLongestSubstring("") == 0, "Empty string failed"
    assert sol.lengthOfLongestSubstring("a") == 1, "Single character failed"
    assert sol.lengthOfLongestSubstring("aa") == 1, "Two same characters failed"
    assert sol.lengthOfLongestSubstring("ab") == 2, "Two different characters failed"

    # LeetCode official examples
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3, "abcabcbb failed"
    assert sol.lengthOfLongestSubstring("bbbbb") == 1, "bbbbb failed"
    assert sol.lengthOfLongestSubstring("pwwkew") == 3, "pwwkew failed"

    # Edge & tricky cases
    assert sol.lengthOfLongestSubstring("dvdf") == 3, "dvdf failed"
    assert sol.lengthOfLongestSubstring("anviaj") == 5, "anviaj failed"
    assert sol.lengthOfLongestSubstring("abba") == 2, "abba failed"
    assert sol.lengthOfLongestSubstring("tmmzuxt") == 5, "tmmzuxt failed"

    # Spaces & symbols
    assert sol.lengthOfLongestSubstring(" ") == 1, "Single space failed"
    assert sol.lengthOfLongestSubstring("a b c a") == 3, "Spaces included failed"
    assert sol.lengthOfLongestSubstring("!@#!!@#") == 3, "Special characters failed"

    print("All local tests passed ✅")
