# 1047. Remove All Adjacent Duplicates In String
# 祖马！
# Stack很适合相邻元素的消消乐


# Stack - 可以用字符串模拟stack 或者python可以用deque双向队列

# 思路Algorithm in Stack
# for val in str
#   if stack is empty OR val != first val in stack:
#       stack add val
#   else: stack remove first val
# return the reversed order of stack if add and pop from left, return stack if from right


# 思路Algorithm in str
# res = ''
# for val in str
#   if res is empty OR val != res[-1]:
#       res += val
#   else:
#       res = res[:-1]
# return res

class Solution:
    # using stack
    def removeDuplicates(self, s: str) -> str:
        res = []
        for c in s:
            if not res:
                res.append(c)
            else:
                val = res.pop()
                if val != c:
                    res.append(val)
                    res.append(c)
        return ''.join(res)

    # using string
    def removeDuplicatesInString(self, s: str) -> str:
        res = ''
        for c in s:
            if not res or c != res[-1]:
                res += c
            else:
                res = res[:-1]
        return res





# Two Pointers
