class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = list(set(nums))
        sorted_nums = sorted(set_nums)
        
        count = 0
        longest = []
        if len(sorted_nums) == 0:
            return 0
        if len(sorted_nums) == 1:
            return 1
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i+1] == sorted_nums[i] + 1:
                count += 1
            elif sorted_nums[i+1] != sorted_nums[i] + 1:
                longest.append(count)
                count = 0
            longest.append(count)
        
        x = max(longest)
        return x + 1
