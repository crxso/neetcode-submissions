class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        left = res = 0

        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            
            my_set.add(s[right])
            res = max(res, right - left + 1)
        
        return res


        # map = {}
        # left = right = res = 0

        # for right in range(len(s)):
        #     if s[right] in map:
        #         left = max(map[s[right]] + 1, left)
        #     map[s[right]] = right
        #     res = max(res, right - left + 1)

        # return res



        