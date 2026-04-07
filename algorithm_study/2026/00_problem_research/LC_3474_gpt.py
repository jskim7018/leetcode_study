class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        L = n + m - 1

        # -------------------------------
        # Step 1: Z-algorithm on str2
        # -------------------------------
        def build_z(s):
            n = len(s)
            z = [0] * n
            l = r = 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            return z

        z = build_z(str2)

        # -------------------------------
        # Step 2: Validate T overlaps
        # -------------------------------
        prev = -1
        for i in range(n):
            if str1[i] == 'T':
                if prev != -1:
                    d = i - prev
                    if d < m and z[d] < m - d:
                        return ""
                prev = i

        # -------------------------------
        # Step 3: Build base word + locked
        # -------------------------------
        word = ['?'] * L
        locked = [False] * L

        last_T = -1
        for i in range(L):
            if i < n and str1[i] == 'T':
                last_T = i
            if last_T != -1 and i < last_T + m:
                word[i] = str2[i - last_T]
                locked[i] = True

        # fill remaining with 'a'
        for i in range(L):
            if word[i] == '?':
                word[i] = 'a'

        # -------------------------------
        # Step 4: Build match_count
        # -------------------------------
        match_count = [0] * n
        for i in range(n):
            cnt = 0
            for j in range(m):
                if word[i + j] == str2[j]:
                    cnt += 1
            match_count[i] = cnt

        # -------------------------------
        # Step 5: Fix F constraints
        # -------------------------------
        for i in range(n):
            if str1[i] == 'F' and match_count[i] == m:
                changed = False

                for j in reversed(range(m)):
                    pos = i + j

                    if locked[pos]:
                        continue  # 🔥 cannot modify T-forced positions

                    old = word[pos]

                    for c in range(ord(old) + 1, ord('z') + 1):
                        new_char = chr(c)
                        word[pos] = new_char

                        updates = []
                        for k in range(max(0, pos - m + 1), min(n, pos + 1)):
                            old_match = (old == str2[pos - k])
                            new_match = (new_char == str2[pos - k])

                            if old_match != new_match:
                                match_count[k] += (1 if new_match else -1)
                                updates.append(k)

                        if match_count[i] < m:
                            changed = True
                            break

                        # revert
                        word[pos] = old
                        for k in updates:
                            match_count[k] += (-1 if new_char == str2[pos - k] else 1)

                    if changed:
                        break

                if not changed:
                    return ""

        return "".join(word)