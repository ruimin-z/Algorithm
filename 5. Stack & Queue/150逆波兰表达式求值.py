# 150. Evaluate Reverse Polish Notation

# 两个数字和一个操作符 进行消除 合成一个数字


from typing import List

def evalRPN(self, tokens: List[str]) -> int:
    ops = ['+', '-', '*', '/']
    stack = []
    for s in tokens:
        if s not in ops: # s is number
            stack.append(int(s))
        else: # s is operations
            num1 = stack.pop()
            num2 = stack.pop()
            match s:
                case '+':
                    stack.append(num1+num2)
                case '-':
                    stack.append(num2-num1)
                case '*':
                    stack.append(num1*num2)
                case '/':
                    stack.append(int(num2/num1))
    return stack.pop()