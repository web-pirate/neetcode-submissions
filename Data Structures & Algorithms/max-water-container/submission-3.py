class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mArea = 0
        left = 0
        right = len(heights)-1
        for i in range(len(heights)):
            short = min(heights[left], heights[right])
            area = short * (right-left)
            if mArea<area:
                mArea = area

            if heights[left] >= heights[right]:
                right = right-1
                continue
            else:
                left = left+1
                continue
        return mArea
        