class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = []
        if len(strs) == 0:
            return "" 
        
        for i in range(len(strs[0])):
            s = None
            count  = 0

            for j in range(len(strs)):
                if i >= len(strs[j]):
                    return "".join(string)
                
                if s is None:
                    s = strs[j][i]
                if s == strs[j][i]:
                    count = count +1
                else:
                    return "".join(string)
            if count == len(strs):
                string.append(s)
        return "".join(string)
        