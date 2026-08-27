class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, n in enumerate(nums):
            new_target = target - n
            if new_target not in indices:
                indices[n] = index
            elif new_target in indices:
                return [indices[new_target], index]
        