from typing import List

# class Solution:
#     def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
#         tmp = []
#         for i in timeSeries:
#             for j in range(i, i + duration):
#                 if j not in tmp:
#                     tmp.append(j)
#         return len(tmp)

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res=0
        for i in range(len(timeSeries)-1):
            res+=min(duration,timeSeries[i+1]-timeSeries[i])

        res+=duration
        return res

timeSeries = [1, 3, 5]
duration = 3
s = Solution()
print(s.findPoisonedDuration(timeSeries, duration))