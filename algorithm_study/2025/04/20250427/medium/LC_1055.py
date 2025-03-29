class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        target_idx = 0
        source_idx = 0

        cnt = 0
        ans = 0
        isFirst = True
        while target_idx < len(target):
            if target[target_idx] == source[source_idx]:
                if isFirst:
                    ans += 1
                    isFirst = False
                target_idx += 1
                source_idx += 1
                cnt = 0
            else:
                source_idx += 1
                cnt += 1
            if cnt == len(source):
                return -1
            if source_idx == len(source):
                source_idx = 0
                isFirst = True

        return ans
