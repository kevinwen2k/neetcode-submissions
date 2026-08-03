class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        out = []
        for s in tokens:
            if s not in ['+', '-', '*', '/']:
                out.append(int(s))
            else:
                result = None
                op2 = out.pop()
                op1 = out.pop()
                if s == '+':
                    result = op1 + op2
                    out.append(result)
                elif s == '-':
                    result = op1 - op2
                    out.append(result)
                elif s == '*':
                    result = op1 * op2
                    out.append(result)
                elif s == '/':
                    result = int(op1 / op2)
                    out.append(result)

        return out.pop()