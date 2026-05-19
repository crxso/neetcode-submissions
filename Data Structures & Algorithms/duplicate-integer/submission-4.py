class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # ans = set(nums)
        # if len(ans) < len(nums):
        #     return True
        # else:
        #     return False
        map = set()
        for num in nums:
            if num in map:
                return True
            else:
                map.add(num)
        
        return False