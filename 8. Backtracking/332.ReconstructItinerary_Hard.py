# 332. Reconstruct Itinerary - https://leetcode.com/problems/reconstruct-itinerary/description/
# Example 1:
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
#
# Example 2:
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.


#               [[A,B],[A,C],[C,A]]   ->   A: [B,C], C:[A]
#                             A->{B,C}
#                       B/              C\
#                  B->{},A->B        C->{A}, A->C
#                                        A|
#                                    A->{B,C}, A->C->A
#                                    B/         C\
#                          B->{}, A->C->A->B      (repeated)
#                                 ✅


# DFS

from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # construct dictionary
        schedule = {}

        tickets.sort(key=lambda x: x[1])  # sort dest in increasing order
        for depart, land in tickets:
            if depart in schedule:
                schedule[depart].append(land)
            else:
                schedule[depart] = [land]

        def backtrack(airport):
            while airport in schedule and schedule[airport]:
                nxt_dest = schedule[airport].pop(0)
                backtrack(nxt_dest)
            res.append(airport)

        res = []
        backtrack("JFK")
        return res[::-1]
