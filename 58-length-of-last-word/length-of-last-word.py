class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splited_str = s.split()
        last_word = splited_str[-1]
        return len(last_word)
        