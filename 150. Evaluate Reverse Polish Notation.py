class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for s in tokens:
            if len(s) == 1 and s[0] in '+-*/':
                num2 = stack.pop()
                num1 = stack.pop()
                if s[0] == '+':
                    stack.append(num1 + num2)
                elif s[0] == '-':
                    stack.append(num1 - num2)
                elif s[0] == '*':
                    stack.append(num1 * num2)
                else:
                    if num1 < 0 and num2 > 0 or num1 > 0 and num2 < 0:
                        stack.append(-(-num1 / num2))
                    else:
                        stack.append(num1 / num2)
            else:
                stack.append(int(s))
        return stack[0]