# https://leetcode.com/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150
from typing import List, Dict

class Solution:

    def trap(self, height: List[int]) -> int:

        left_view = height[:]
        right_view = height[:]

        for i in range(1, len(left_view)):
            left_view[i] = max(left_view[i-1], left_view[i])

        for i in range(len(right_view) - 2, -1, -1):
            right_view[i] = max(right_view[i+1], right_view[i])

        trapped_water = 0

        for i in range(len(height)):
            trapped_water += (min(left_view[i], right_view[i]) - height[i])

        return trapped_water