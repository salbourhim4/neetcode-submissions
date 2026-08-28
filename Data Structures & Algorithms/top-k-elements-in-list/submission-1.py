class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> list[int]:
        frequency = {}
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        descending_value = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        sol = list(descending_value)[:k]
        return sol
            

