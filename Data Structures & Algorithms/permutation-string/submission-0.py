class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding windows
        left = 0
        d_c = {}
        for j in range(0, len(s1)):
            d_c[s1[j]] = d_c.get(s1[j],0)+1    
        d ={}
        for i in range(len(s2)):
            d[s2[i]] = d.get(s2[i],0)+1
            if i-left+1 == len(s1):
                if d_c==d:
                    return True
                d[s2[left]]=d.get(s2[left])-1               
                if d[s2[left]] == 0:
                    del d[s2[left]]#hanging key

                left+=1

        return False

        #conditions for moving the window is false

        #s1 alpahbetical order/or use a dictionary for the frequency values
        
