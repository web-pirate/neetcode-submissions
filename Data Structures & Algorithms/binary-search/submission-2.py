class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = int((left + right)/2)
        for i in range(len(nums)):
            print(mid)
            if nums[mid] == target: 
                return nums.index(nums[mid])
            elif nums[left] == target:
                return nums.index(nums[left])
            elif nums[right] == target:
                return nums.index(nums[right])
            elif nums[mid] > target:
                right = mid
                mid = int((left + right)/2)
            else:
                left = mid
                mid = int((left + right)/2)
        return -1

