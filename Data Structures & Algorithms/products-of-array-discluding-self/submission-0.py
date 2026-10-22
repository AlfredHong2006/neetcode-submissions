class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #find product of all, heap/dict/list/hashmap
        #O(n)requires O(1) for each x 'n'
        #after a value is "seen", you store it in the dictionary.

        # l = len(nums)
        # a = [1]*l
        # b = [1]*l

        # for i in range(1, l): #stop is never filled
        #     a[i] = nums[i-1]*a[i-1]
        # for j in range(l-2, -1, -1): #stop at 0
        #     b[j] = nums[j+1]*b[j+1]
        
        # return [i * j for i,j in zip(a,b)]

        l = len(nums)
        ans = [1]*l
        for i in range(1,l):
            ans[i] = ans[i-1]*nums[i-1]
        right = 1
        for io in range(l-1, -1, -1):
            ans[io]*= right
            right *= nums[io]
        return ans