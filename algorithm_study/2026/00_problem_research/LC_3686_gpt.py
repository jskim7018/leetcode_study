class Solution:
    def countStableSubsequences(self, nums):
        # TODO: dictionary DP 보다 훨씬 빠름. 자세히 공부 필요함.
        # TODO: subsequence를 구한다 등은 경우의 수를 구한다와 비슷하다.
        # TODO: 이전 상태들을 모아두고 현재 상태 기반 이전 가능한 것들의 경우의 수를 축정한다.
        MOD = 10 ** 9 + 7

        '''
        even1: last element even, but previous is odd or none
        even2: last two are even   
        similarly for odd
        '''
        even1 = even2 = 0
        odd1 = odd2 = 0

        for x in nums:
            if x % 2 == 0:
                # Save old values
                new_even2 = even1  # 현재가 even이니깐 모든 even1있는것 됨.
                new_even1 = (odd1 + odd2 + 1) % MOD  # 현재가 even니깐 모든 odd 됨.

                even1 = (even1 + new_even1) % MOD
                even2 = (even2 + new_even2) % MOD
            else:
                new_odd2 = odd1
                new_odd1 = (even1 + even2 + 1) % MOD

                odd1 = (odd1 + new_odd1) % MOD
                odd2 = (odd2 + new_odd2) % MOD

        return (even1 + even2 + odd1 + odd2) % MOD
