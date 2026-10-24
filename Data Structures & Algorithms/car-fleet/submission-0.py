class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #distance left = target - position
        #two cars cross if time to fleet for the car further behind is < t_car(furtheralong)
        #time = distance/speed
        info = {}
        value=0
        t_previous = 0
        for i in range(len(position)):
            info[position[i]] =  (target-position[i])/(speed[i])
        info = sorted(info.items(), reverse = True)
        for p, t in info:
            if t_previous < t:
                value+=1
                t_previous = t
        return value
        
        