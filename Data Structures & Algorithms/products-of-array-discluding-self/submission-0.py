class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        value = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    value = value * nums[j]
            out.append(value)
            value = 1
        return out
        