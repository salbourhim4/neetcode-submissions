class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rlist = []
        for item in nums:
            if item not in rlist:
                rlist.append(item)
        if len(rlist) != len(nums):
            return True
        else:
            return False
         