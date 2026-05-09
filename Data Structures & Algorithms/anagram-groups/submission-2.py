class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_table = defaultdict(list)
        for s in strs:
            key = [0 for _ in range(26)]
            for char in s:
                key[ord(char) - ord("a")] += 1
            hash_table[tuple(key)].append(s)
        
        return list(hash_table.values())
        


                
                
