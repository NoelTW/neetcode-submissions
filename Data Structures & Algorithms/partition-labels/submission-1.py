class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        seen = defaultdict(int)
        ans = []
        l = 0
        for r, c in enumerate(s):
            seen[c] += 1
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]
            is_valid = True
            for key in seen:
                if key in counter:
                    is_valid = False
            if is_valid:
                ans.append(r - l + 1)
                l = r + 1
        return ans