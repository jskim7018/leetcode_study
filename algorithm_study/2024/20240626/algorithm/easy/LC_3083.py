from copy import copy


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        s_rev = s[::-1] # reverse는 이렇게 할 수 있음.
        for i in range(len(s)-1):
            # if s_rev.find(s[i:i+2]) != -1: # 못찾을 시 -1 반환
            #     return True
            if s[i:i+2] in s_rev: # in으로도 substring 포함여부 확인 가능
                return True
        return False
