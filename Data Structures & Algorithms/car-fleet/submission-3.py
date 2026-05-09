class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        car 0 > 1, 4, 7, 10
        car 1 > 4, 6, 8, 10
        """
        stack= []
        for p, s in sorted(((p,s) for p,s in zip(position, speed)), reverse=True):
            t = (target - p) / s
            if stack and stack[-1] >= t:
                continue
            stack.append(t)
        return len(stack)
             