# 20. Valid Parentheses

# 遇到匹配左右括号 进行消除

# 算法Algorithm using Stack - 遇到左括号，把其对应的右括号加入stack中，遇到右括号，和stack pop出的元素比较
# for bracket in str:
#   if bracket is in left set:
#      stack add corresponding right bracket
#   else: # bracket in right set, compare with stack.pop()
#      if stack is null: return false # 左括号少
#      if bracket mismatch stack.pop(): return false  # 开和闭不一样
# if stack is not null: return false # 左括号多
# return true

# 三种不匹配的情况Three mismatch situations:
# 1. 字符串遍历完毕，但stack不为空 - 左括号多
# 2. stack为空，但字符串未遍历完毕 - 左括号少
# 3. stack和字符串当前值不匹配

from collections import deque

def isValid(s: str) -> bool:
    stack = deque()
    bracket_pairs = {'(' : ')', '[':']', '{':'}'}
    for b in s:
        if b in bracket_pairs:
            stack.append(b)
        elif not stack or stack.pop() != bracket_pairs[b]:
            return False
    return True if not stack else False  # will return after iterating if the stack is emptyu



## 题外话
# 括号匹配是使用栈解决的经典问题。
# 题意其实就像我们在写代码的过程中，要求括号的顺序是一样的，有左括号，相应的位置必须要有右括号。
# 如果还记得编译原理的话，编译器在 词法分析的过程中处理括号、花括号等这个符号的逻辑，也是使用了栈这种数据结构。
# 再举个例子，linux系统中，cd这个进入目录的命令我们应该再熟悉不过了。
# cd a/b/c/../../
# 这个命令最后进入a目录，系统是如何知道进入了a目录呢 ，这就是栈的应用（其实可以出一道相应的面试题了）
# 所以栈在计算机领域中应用是非常广泛的。
# 有的同学经常会想学的这些数据结构有什么用，也开发不了什么软件，大多数同学说的软件应该都是可视化的软件例如APP、网站之类的，那都是非常上层的应用了，底层很多功能的实现都是基础的数据结构和算法。
# 所以数据结构与算法的应用往往隐藏在我们看不到的地方！




# ----------- previous submit ----------- #

def isValid_prev(s: str) -> bool:
    if not s:
        return True
    lst = [] # use stack is good as well
    for p in s:
        if p in ['(', '{', '[']: # use dict is better
            lst.append(p)
        else:
            if len(lst) == 0: return False
            last_open = lst[-1]
            if (last_open=='{' and p =='}') or (last_open=='[' and p ==']') or (last_open=='(' and p ==')'):
                lst = lst[:-1]
                continue
            else:
                return False
    return len(lst) == 0