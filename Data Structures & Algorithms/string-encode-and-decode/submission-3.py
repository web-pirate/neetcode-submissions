class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        for strs_value in strs:
            s += str(len(strs_value))
            s += "#"
            s += strs_value
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        de = []
        n = len(s)
        i = 0

        while i < n:
            length = 0
            

            while s[i] != "#":
                length = length * 10 + (ord(s[i]) - ord("0"))
                i = i + 1
            
            i = i+1

            string = s[i:i+length]
            de.append(string)

            i = i+length
        return de

