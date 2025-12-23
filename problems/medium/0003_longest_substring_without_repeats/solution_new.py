"""
LeetCode 0003: longest substring without repeats
Difficulty: Medium
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) in [0, 1]:
            return len(s)

        char_locs = {}
        max_len = 0
        pointer_left: int = 0
        pointer_right: int = 0
        # print(f"\nStarting test for string: {s}")
        # print(f"pointer_left: {pointer_left}, pointer_right: {pointer_right}")

        while pointer_right < len(s):
            # print(f"\npointer_left: {pointer_left} at {s[pointer_left]}")
            # print(f"pointer_right: {pointer_right} at {s[pointer_right]}")
            if s[pointer_right] not in char_locs.keys():
                # print(f"{s[pointer_right]} not in char_locs.key()")

                char_locs[s[pointer_right]] = pointer_right

            elif (
                s[pointer_right] in char_locs
                and char_locs[s[pointer_right]] >= pointer_left
            ):
                pointer_left = char_locs[s[pointer_right]] + 1
                char_locs[s[pointer_right]] = pointer_right

            else:
                char_locs[s[pointer_right]] = pointer_right

            current_len = pointer_right - pointer_left + 1
            if current_len > max_len:
                max_len = current_len

            pointer_right += 1

        # print(
        #     f"after loop -> pointer_left: {pointer_left}, pointer_right: {pointer_right}"
        # )
        #
        # print(f"max_len: {max_len}")
        return max_len


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

    # Other
    assert sol.lengthOfLongestSubstring("aabaab!bb") == 3, "Other failed"

    print("All local tests passed ✅")
