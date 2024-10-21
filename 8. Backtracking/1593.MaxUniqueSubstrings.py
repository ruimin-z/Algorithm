# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/


#                  aba
#           a/      \ab      \aba
#        {a},ba     {ab},a    {aba}
#       b/    \ba      \a
#   {a,b},a   {a,ba}   {ab,a}
#     a/
#  {a,b,a}

# 1. identify the params in backtracking
#    start index, a set of seen elements
# 2. identify the termination condition
#    if start index reaches to the end, return the current unique set length
# 3. identify the choices at each level
#    end index defining substring

# Find the max count of unique substrings
def maxUniqueSplit(s: str) -> int:
    # 1. why return int?
    # Want to return the number max count of substrings within the string starting from index start
    def backtrack(start, seen) -> int:
        if start == len(s):
            return 0 # 2. why 0? Due to addition, return only 0 when reached to the end
        max_count = 0 # 3. why initialization? Initialize max_count to 0 each time due to addition on each level
        for end in range(start+1, len(s)+1):
            substr = s[start:end]
            if substr not in seen:
                seen.add(substr)
                # 4. why? Explore all possible counts of unique substrings
                # where the first split is substr each time, and take the max
                max_count = max(max_count, 1 + backtrack(end, seen))
                seen.remove(substr)
        return max_count
    return backtrack(0, set())

print(maxUniqueSplit("ababccc"))
print(maxUniqueSplit("wwwzfvedwfvhsww"))

# Find the set with maximum unique substrings
# 1. we dont need a 2D array, so no append, so either return or need to pass in max count set as param.
# If pass in as param, change its value, but never return it, then value is lost. So must return.
# 2. Then we must copy the result, otherwise, it is not constant
def maxUniqueSplit_alternative(s: str) -> int:
    def backtrack_alternative(seen, start, max_count_seen):
        if start >= len(s):
            if len(seen) > len(max_count_seen):
                max_count_seen = seen.copy() # must copy, otherwise it's only reference to seen, and changes as seen changes (add and pop)
            return max_count_seen
        for end in range(start + 1, len(s) + 1):
            substr = s[start:end]
            if substr not in seen:
                seen.add(substr)
                max_count_seen = backtrack_alternative(seen, end, max_count_seen)
                seen.remove(substr)
        return max_count_seen
    max_count_seen = backtrack_alternative(set(), 0, set())
    return len(max_count_seen)


print(maxUniqueSplit_alternative("ababccc"))
print(maxUniqueSplit_alternative("wwwzfvedwfvhsww"))
