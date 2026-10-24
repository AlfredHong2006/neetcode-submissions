class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #how many mutliple times?
        over = h-len(piles)
        left,right = 1, max(piles)
        m =0
        if over == 0:
            return max(piles)
        else:
            while left<right:
                total =0
                middle = (left+right)//2

                for i in range(len(piles)):
                    total +=(piles[i] + middle-1)//middle #or math.ceil(piles[i], middle) total += piles[i]//middle
                     
                if total>h:
                    left = middle+1
                else:
                    right = middle

            return right