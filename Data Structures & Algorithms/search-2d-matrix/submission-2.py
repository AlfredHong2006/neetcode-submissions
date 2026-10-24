class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,right= 0, len(matrix)
        left2,right2 = 0, len(matrix[0])
        #answer runs in one pass


        #compare the last element of each row, do binary search to narrow it down
        #compare the values with binary seasrch.

        if target > matrix[-1][-1]:
            return False
        while left < right:
            middle = int((left + right)/2)
            if matrix[middle][-1]<target:
                left = middle+1
            elif matrix[middle][-1]>target:
                right = middle
            else:
                return True
        
        while left2 < right2:
            middle2 = int((left2 + right2)/2)
            if matrix[left][middle2]<target:
                left2 = middle2+1
            elif matrix[left][middle2]>target:
                right2 = middle2
            else:
                return True
        return False