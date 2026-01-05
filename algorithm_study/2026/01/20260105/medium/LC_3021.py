class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_odd_cnt = n//2
        n_even_cnt = n//2
        if n % 2 == 1:
            n_odd_cnt += 1
        m_odd_cnt = m//2
        m_even_cnt = m//2
        if m % 2 == 1:
            m_odd_cnt += 1

        return n_odd_cnt * m_even_cnt + m_odd_cnt * n_even_cnt
