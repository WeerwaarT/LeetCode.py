# 2651. 计算列车到站时间
# https://leetcode.cn/problems/calculate-delayed-arrival-time/


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24