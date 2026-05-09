class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track_table = {}
        for s in strs:
            s_list = list(s)
            s_list.sort()
            if tuple( s_list )  not in track_table:
                track_table[tuple(s_list)] = [s]
            else:
                track_table[tuple(s_list)].append(s)
        
        final = []

        for val in track_table.values():
            final.append(val)

        return final
            