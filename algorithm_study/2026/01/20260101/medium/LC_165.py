class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        split_version1 = version1.split(sep='.')
        split_version2 = version2.split(sep='.')

        n_ver1 = len(split_version1)
        n_ver2 = len(split_version2)

        for i in range(max(n_ver1, n_ver2)):
            int_v1, int_v2 = 0, 0
            if i < n_ver1:
                int_v1 = int(split_version1[i])
            if i < n_ver2:
                int_v2 = int(split_version2[i])
            if int_v1 > int_v2:
                return 1
            elif int_v1 < int_v2:
                return -1
        return 0
