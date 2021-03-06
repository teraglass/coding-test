# 해시 테이블을 이용한 풀이
import collections


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = {}
        count = 0

        # 돌(S)의 빈도 수 계산
        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        # 보석(J)의 빈도 수 계산
        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count

# defaultdict를 이용한 비교 생략
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        # 비교 없이 돌 빈도 수 계산
        for char in S:
            freqs[char] += 1

        # 비교 없이 보석 빈도 수 합산
        for char in K:
            count += freqs[char]
        return count
    
# Counter로 계산 생략
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.Counter(S) # 돌 빈도 수 계산
        count = 0

        # 비교 없이 보석 빈도 수 합산
        for char in J:
            count += freqs[char]

        return count

# 파이썬다운 방식

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)