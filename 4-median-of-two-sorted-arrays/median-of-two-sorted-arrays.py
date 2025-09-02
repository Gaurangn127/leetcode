class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A) :
            A, B = B, A
         
        m, n = len(A), len(B)           # m <= n
        total = (m + n)
        half = total // 2

        left, right = 0, (m - 1)

        while True :
            i = (left + right) // 2
            j = half - i - 2                    # -2 because arrays are 0-indexed

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if (i + 1) < m else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j + 1] if (j + 1) < n else float('infinity')

            if Aleft <= Bright and Bleft <= Aright :
                if total % 2 == 1 :
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright :
                right = i - 1
            
            else :
                left = i + 1