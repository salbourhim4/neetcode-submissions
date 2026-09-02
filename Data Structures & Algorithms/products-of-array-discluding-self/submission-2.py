class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rlist = [1] * len(nums)
        prefix = [1] * len(nums)
        running1 = 1
        for i in range(len(nums)):
            prefix[i] = running1
            running1 *= nums[i]

        suffix = [1] * len(nums)
        running2 = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = running2
            running2 *= nums[i]

        for i in range(len(nums)):
            rlist[i] = prefix[i] * suffix[i]

        return rlist

        