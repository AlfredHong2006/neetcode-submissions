class Solution:
    def trap(self, height: List[int]) -> int:
        
        #brute force edition
        # water = 0
        # for column in range(len(height)):
        #     #find max of right/left, take the shorter and subtract by itself
        #     if column != 0 and column != len(height):
        #         left, right = max(height[:column+1]), max(height[column:])
        #         water += min(left,right) - height[column]
        # return water
        l,r = 0, len(height)-1
        left_max, right_max = height[0], height[-1]
        area = 0
        while l<r:
            if left_max <right_max:
                l+=1
                left_max = max(height[l], left_max)
                area += left_max-height[l]
            else:
                r-=1
                right_max = max(height[r], right_max)
                area += right_max-height[r]
        return area

