class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        seen = []
        result = 0
        op = ["+","*", "-", "/"]
        if len(tokens) == 1:
            return int(tokens[0])
        for i in range(len(tokens)):
            if tokens[i] in op:
                value1 = seen.pop()
                value2 = seen.pop()
                exp = f"{value2} {tokens[i]} {value1}"
                exp = int(eval(exp))
                result = exp
                seen.append(exp)
            else:
                seen.append(tokens[i])
        return int(result)
            
        