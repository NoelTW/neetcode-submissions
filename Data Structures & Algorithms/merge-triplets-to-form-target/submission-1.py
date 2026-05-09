class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        is_a, is_b, is_c = False, False, False
        for a, b, c in triplets:
            if any((a > x, b > y, c > z)):
                continue
            if a == x:
                is_a = True
            if b == y:
                is_b = True
            if c == z:
                is_c = True
        return all((is_a, is_b, is_c))