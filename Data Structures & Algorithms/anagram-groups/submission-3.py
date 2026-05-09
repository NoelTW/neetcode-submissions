class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = {}
        for string in strs:
            counter = [0] * 26

            for char in string:
                counter[ord(char) - ord("a")] += 1

            if tuple(counter) not in ans_dict:
                ans_dict[tuple(counter)] = [string]
            else:
                ans_dict[tuple(counter)].append(string)
        ans = []
        for val in ans_dict.values():
            ans.append(val)
        
        return ans
            

            