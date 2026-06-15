class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        for i in range(1, len(numbers)):
            s = numbers[left] + numbers[right]
            if s > target:
                right = right-1
            elif s < target:
                left = left + 1
            else:
                return [left+1, right+1]
             