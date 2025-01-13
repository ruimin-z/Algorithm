#              aab
#        a/   \a      \b
#       a|ab   aa|b    aab| ✓
#      a/  \b      \b
#    a|a|b  a|ab|  aa|b|
#    b/
#  a|a|b| ✓


# start index is the beginning index of unsplit substring
# i marks the split line "|" in the tree
# if the split line is at the end, then get a leaf node (one splitting solution)

from typing import List

def partition(s: str) -> List[List[str]]:
    def backtrack(s, start_index):
        if start_index == len(s):
            res.append(path[:]) # collected to res
            return
        for i in range(start_index, len(s)):
            substring = s[start_index:i+1]
            if substring == substring[::-1]: # is Palindrome
                path.append(substring)
                backtrack(s, i + 1)  # i marks the last index of the previous palindrome found
                path.pop()  # choose another path
    path = [] # 1D array - one possible palindrome solution
    res = []  # 2D array - all palindrome solutions
    backtrack(s,0)
    return res


# path + [s[start:end]] - does not change path reference, so no need to pop or append

def partition_alternative(s: str) -> List[List[str]]:
    def backtrack_alternative(path, start):
        if start == len(s):
            # collected to res.
            # append() changes result reference directly, so no need to pass in result as param
            result.append(path[:])
            return
        for end in range(start+1, len(s)+1):
            substring = s[start:end]
            if substring == substring[::-1]: # is Palindrome
                backtrack_alternative(path + [s[start:end]], end)  # end marks the (last index + 1) of the previous palindrome found
    result = [] # 2D array - all palindrome solutions
    backtrack_alternative([],0)
    return result

print(partition('aab'))


print(partition_alternative('aab'))