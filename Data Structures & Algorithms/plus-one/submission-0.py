class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        digits[-1] += 1
        for i in range(n- 1, -1, - 1):
            dig = digits[i]
            dig += carry
            digits[i] = dig % 10
            carry = dig // 10
        if carry:
            return [carry] + digits
        return digits
