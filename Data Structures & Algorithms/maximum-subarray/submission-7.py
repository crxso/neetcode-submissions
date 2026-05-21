class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curSum = nums[0], 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(curSum, maxSum)
        return maxSum

        # left = curr = 0
        
        # max_sum = 0
        # for i in range(1):
        #     max_sum += nums[i]
        # longest = max_sum

        # for right in range(len(nums)):
        #     curr += nums[right]
        #     while curr < max_sum:
        #         max_sum -= nums[left]
        #         max_sum += nums[right]
            
        #     longest = max(longest, max_sum)
        
        # return longest

# 1st iteration
# longest = 2
# max_sum = 2
# curr = 2

# 2nd iteration
# longest = 2
# max_sum = 1
# curr = -1

# 3rd iteration
# longest = 2
# max_sum = -2
# curr = 3


