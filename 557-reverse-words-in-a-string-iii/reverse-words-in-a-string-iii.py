class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        new = [i[::-1] for i in word]
        reverseWords = " ".join(new)
        return reverseWords
        