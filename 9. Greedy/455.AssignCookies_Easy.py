# 455. Assign Cookies - https://leetcode.com/problems/assign-cookies/description/
#
# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
#
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
#
#
# Example 1:
# Input: g = [1,2,3], s = [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.
#
# Example 2:
# Input: g = [1,2], s = [1,2,3]
# Output: 2
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
# You have 3 cookies and their sizes are big enough to gratify all of the children,
# You need to output 2.
#
#
# Constraints:
#     1 <= g.length <= 3 * 104
#     0 <= s.length <= 3 * 104
#     1 <= g[i], s[j] <= 231 - 1

# sort first
# [g1,g2,g3,...,gk] s.t. g1<=g2<=...<=gk
# [s1,s2,s3,...,sk] s.t. s1<=s2<=...<=sk

from typing import List

################################# Greedy with Two Pointers
##### "big cookie for big kid"
#### but can also follow logic of "small cookie for small kid"

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_id,s_id=len(g)-1,len(s)-1
        value = 0
        while g_id >= 0 and s_id >= 0:
            # s[j] < g[i]
            while g_id >= 0 and s[s_id] < g[g_id]:
                g_id-=1
            # no g anymore
            # Since sorted, if current s_j cannot satisfy any g, then all the preceding s (smaller than s_j) cannot satisfy either
            # Stop the search
            if g_id < 0:
                break
            # s[j] >= g[i]
            value += 1
            s_id -= 1
            g_id -= 1
        return value


################################# Greedy with one pointer

class Solution2:
    def findContentChildren(self, g, s):
        g.sort()  # 将孩子的贪心因子排序
        s.sort()  # 将饼干的尺寸排序
        index = 0
        for i in range(len(s)):  # 遍历饼干
            if index < len(g) and g[index] <= s[i]:  # 如果当前孩子的贪心因子小于等于当前饼干尺寸
                index += 1  # 满足一个孩子，指向下一个孩子
        return index  # 返回满足的孩子数目



