from typing import List


class Solution:
    # 3 possible cases:
    #   1: left partition entirely on smaller array
    #   2: left partition shared between smaller and larger array
    #   3: left partition entirely on larger array
    # depending on if merged array is odd or even...
    #   case 1:
    #       even: size of two arrays will be equal
    #       odd: larger array size greater by 1
    #   case 2:
    #       even or odd: size difference is variable
    #   case 3:
    #       even or odd: larger array is larger

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, big = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            small, big = nums2, nums1

        l, r = 0, len(small) - 1

        while True:
            i = (l + r) // 2
            j = half - (i + 1) - 1

            smallLeft = small[i] if i >= 0 else float("-infinity")
            smallRight = small[i + 1] if i + 1 < len(small) else float("infinity")
            bigLeft = big[j] if j >= 0 else float("-infinity")
            bigRight = big[j + 1] if j + 1 < len(big) else float("infinity")

            if smallLeft <= bigRight and bigLeft <= smallRight:
                # odd
                if total % 2:
                    return min(smallRight, bigRight)

                # even
                return (max(smallLeft, bigLeft) + min(smallRight, bigRight)) / 2
            elif smallLeft > bigRight:
                r = i - 1
            # bigLeft > smallRight
            else:
                l = i + 1

