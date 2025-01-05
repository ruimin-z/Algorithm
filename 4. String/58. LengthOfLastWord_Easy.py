class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last_space_index = s[::-1].find(' ')
        # print(last_space_index)
        if last_space_index == -1:
            return len(s)
        return last_space_index

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         words = s.strip().split()
#         if not words:
#             return 0
#         return len(words[-1])