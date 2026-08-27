class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = []
        indices = {}
        for n in strs:
            new_strs.append("".join(sorted(n)))

        for index, n in enumerate(new_strs):
            if n not in indices:
                indices[n] = []
            indices[n].append(index)

        solution1 = []
        solution2 = []
        for value in indices.values():
            for i in value:
                solution1.append(strs[i])
            solution2.append(solution1)
            solution1 = []

        return solution2