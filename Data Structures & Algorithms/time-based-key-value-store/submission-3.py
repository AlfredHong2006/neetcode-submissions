class TimeMap:

    def __init__(self):
        self.container = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.container:
            self.container[key] = []
        self.container[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        if key in self.container:
            
            left, right = 0, len(self.container[key])-1
            while left<=right:
                middle = (left+right)//2
                if self.container[key][middle][1] <= timestamp:
                    res = self.container[key][middle][0]
                    left = middle+1
                else:
                    right = middle -1
        return res




        #     for i in range(len(self.container[key])):
        #         if self.container[key][i][1] <= timestamp:

        #             if i == len(self.container[key]) -1:
        #                 return self.container[key][i][0]
        #             else:
        #                 if self.container[key][i+1][1] > timestamp:
        #                     return self.container[key][i][0]
        
        # return ""
                    # if self.container[key][i][1] > maxmin_time:
                    #     maxmin_time = max(maxmin_time, self.container[key][i][1])
                    #     maxmin_index = i
        # return self.container[key][maxmin_index][0] if key in self.container else ""

        #implement binary search for timestamp
