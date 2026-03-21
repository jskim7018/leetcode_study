from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # min, max, mean, mode -> 1 pass 가능
        # median -> 2 pass (사이즈를 알아야 하기에)
        # => median 2pass 시 작은 것을 새로 만든다. (중간에 빈공감 최소화)

        _min = float('inf')
        _max = float('-inf')
        _mean = 0
        _mode = -1
        _mode_freq = 0
        _median = 0

        total_size = 0
        num_to_count = []

        for i, cnt in enumerate(count):
            if cnt == 0:
                continue
            num_to_count.append((i, cnt))

            if _min == float('inf'):
                _min = i
            _max = i
            _mean += i * cnt

            if cnt > _mode_freq:
                _mode = i
                _mode_freq = cnt

            total_size += cnt

        _mean = _mean / total_size

        if total_size % 2 == 1:
            median_locs = [total_size//2]
        else:
            median_locs = [total_size//2-1, total_size//2]

        curr_cnts = 0
        _median = 0
        med_loc_idx = 0
        for num,cnt in num_to_count:
            curr_cnts += cnt

            while med_loc_idx < len(median_locs):
                if median_locs[med_loc_idx] < curr_cnts:
                    _median += num
                    med_loc_idx += 1
                else:
                    break

            if med_loc_idx >= len(median_locs):
                break

        return [_min, _max, _mean, _median/len(median_locs), _mode]
