
# old solution (slow)
# class Solution:
#     def __init__(self):
#         self.charList = []
#
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
#
#         maxCount = 0
#         count = 0
#         for startIndex, startChar in enumerate(s):
#             count += 1
#             self.charList.append(startChar)
#             if startIndex < len(s) - 1:
#                 for curIndex, curChar in enumerate(s[startIndex + 1:]):
#                     if curChar in self.charList:
#                         break
#                     self.charList.append(curChar)
#                     count += 1
#             if count > maxCount:
#                 maxCount = count
#             self.charList = []
#             count = 0
#         return maxCount


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLength = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
