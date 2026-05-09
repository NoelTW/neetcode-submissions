class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total_len = len(nums1) + len(nums2)
        half = total_len // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            m = l + (r - l) // 2
            A_left = A[m] if m >= 0 else -float('inf')
            A_right = A[m + 1] if (m + 1) < len(A) else float('inf')
            B_left = B[ half - m - 2] if (half - m - 2) >= 0 else -float('inf')
            B_right = B[ half - m - 1 ] if (m + 1) < len(B) else float('inf')

            if A_left <= B_right and B_left <= B_right:
                # Odd
                if total_len % 2:
                    return min(B_right, A_right) 
                
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            elif A_left > B_right:
                r = m - 1
            else:
                l = m + 1
            
            
"""
Example 2:

Input: nums1 = [1,3], nums2 = [2,4]
m = 0
half = 4 // 2 = 2
B_left = half - m - 2 = 2 - 0 - 2 = 0
0 
Output: 2.5
"""