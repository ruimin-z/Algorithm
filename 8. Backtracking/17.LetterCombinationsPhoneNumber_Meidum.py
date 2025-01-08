# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
#
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Example 2:
# Input: digits = ""
# Output: []
#
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]
#
# Constraints:
#     0 <= digits.length <= 4
#     digits[i] is a digit in the range ['2', '9']

# ----------------------------------------------------
# Brute Force: multiple layers of for loop
# Backtrack:
# e.g. digits='23'
#                       [abc]
#             a/         b|          c\
#        a,[def]        b,[def]       c,[def]
#      d/ e| f\       /   |   \        /  |  \
#    [ad] [ae] [af] [bd] [be] [bf]  [cd] [ce] [cf]

# Logic:
# (key: think about each layer set, and use index to get digit)
# - multiple sets of numbers
# - at each layer, get digit at index, get the letters set corresponding with that digit
# - traverse through the letter set,
#       - push current letter
#       - backtrack with index + 1
#       - remove current letter

# Optimization:
# 1. backtrack for loop content can be shortened to one line of code, due to string data structure
# 2. use list rather than dictionary to store mapping

from typing import List

class Solution:
    mapping = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8:'tuv', 9:'wxyz'}
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        def backtrack(digits, index, s):
            if index == len(digits):
                result.append(s)
                return
            digit = int(digits[index]) # digits is a string
            for letter in self.mapping[digit]:
                s += letter
                backtrack(digits, index + 1, s)
                s = s[:-1]

        backtrack(digits, 0, '')
        return result


    mapping_another = ['', '', 'abc', 'def', 'ghi','jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    def letterCombinations_optimized(self, digits: str) -> List[str]:
        if not digits: return []
        result = []
        def backtrack(digits, index, s):
            if index == len(digits):
                result.append(s)
                return
            digit = int(digits[index]) # digits is a string
            for letter in self.mapping[digit]:
                backtrack(digits, index + 1, s + letter) # optimization

        backtrack(digits, 0, '')
        return result