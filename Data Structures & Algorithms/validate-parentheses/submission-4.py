class Solution:
    def isValid(self, s: str) -> bool:
        right = ["[", "{", "("]
        left = ["]", "}", ")"]
        brac = []
        for i in s:
            if i in right:
                brac.append(i)
            else:
                if len(brac) ==0:
                    return False
                last =  brac.pop()
                if right.index(last) == left.index(i):
                    continue
                else:
                    return False
        if len(brac) == 0:
            return True
        else:
            return False