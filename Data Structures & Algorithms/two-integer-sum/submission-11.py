class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        # nums = [3,4,5,6], target = 7

        for i, num in enumerate(nums):
            # i = 1; num = 4
            c = target - num
            # c = 3
            if c in hash_map:
                return [hash_map[c], i] 
            hash_map[num] = i