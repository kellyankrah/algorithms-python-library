from typing import List, Optional
def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    seen = {}
    for i, v in enumerate(nums):
        j = seen.get(target - v)
        if j is not None:
            return [j, i]
        seen[v] = i
    return None
def max_subarray(nums: List[int]) -> int:
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
