# -*- coding: utf-8 -*-
# 투 포인터를 이용한 스왑
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# 파이써닉
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]