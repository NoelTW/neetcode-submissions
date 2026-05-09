class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char) - ord("a")] += 1
            if tuple(key) in res:
                res[tuple(key)].append(string)
            else:
                res[tuple(key)] = [string]

        return [val for val in res.values()]