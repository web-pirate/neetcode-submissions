class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = int((left + right)/2)
        for i in range(len(nums)):
            print(mid)
            if nums[mid] == target: 
                return mid
            elif nums[mid] > target:
                right = mid - 1
                mid = int((left + right)/2)
            else:
                left = mid + 1
                mid = int((left + right)/2)
        return -1

