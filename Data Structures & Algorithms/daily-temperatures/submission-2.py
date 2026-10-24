class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        d = [0]*len(temperatures)
        stack = [] #holds the days: indices that are waiting for a warmer day
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                d[stack[-1]] = i - stack[-1]
                stack.pop(-1)
            stack.append(i)
        return d