class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in my_map:
                return [my_map[compliment], i]
            
            my_map[num] = i

                
