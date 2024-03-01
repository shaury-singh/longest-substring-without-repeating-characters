class Solution:
    def notRepeating(s:str) -> bool:
        arr = list(s)
        setStr = set(list(s))
        if len(arr) == len(setStr):
            return True
        else:
            return False
    def findMax(arr:list[int]) -> int:
        max = 0
        for i in arr:
            if i > max:
                max = i
        return max
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        lengthArr = []
        strArr = []
        while right<=len(s):
            if Solution.notRepeating(s[left:right]) == True:
                lengthArr.append(len(s[left:right]))
                right += 1
            else:
                left += 1
        maximum = Solution.findMax(lengthArr)
        return maximum
