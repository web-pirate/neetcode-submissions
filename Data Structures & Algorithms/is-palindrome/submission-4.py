class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        unw = ["?",",","'",".", ":"]
        for i in s:
            if i in unw:
                s = s.replace(str(i), "")
        if s == s[::-1]:
            return True
        return False
        
            

