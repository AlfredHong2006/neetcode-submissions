class Solution:
    def findMin(self, nums: list[int]) -> int:
        #array rotated between 1 -> n times. 
        #return the minimum element of the array

        #use binary search to find where it changes
        #O(N)
        #return the minimum value

        left, right = 0, len(nums)-1

        while left< right:
            middle = (left+right)//2

            if nums[middle] > nums[right]:
                #slightly different to usual because here we don't find a "value", we are looking for hte lowest value
                left = middle+1
            else:
                right = middle

        return nums[left]