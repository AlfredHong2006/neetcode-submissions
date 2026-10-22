class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #find whever letter is most common currently, replace that letter wtih 

        # d = {}
        # for i in range(len(s)):
        #     d[s[i]]= d.get(s[i], 0)+1
        # if k + d[max(d, key=d.get)] >len(s):
        #     return len(s)
        # return d[max(d, key=d.get)]+k

    #axaxa

    #sliding window
    #list
    #left/right
    #increase left if right is invalid
    #increase r every step

        d = {}
        m, left = 0, 0
        for i in range (len(s)):

            d[s[i]] = d.get(s[i], 0)+1
            while i-left+1 - max(d.values())>k:
                d[s[left]]= d.get(s[left])-1
                left+=1
            m = max(m, i-left+1)
        return m
                