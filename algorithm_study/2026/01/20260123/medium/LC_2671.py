from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.num_to_freq = defaultdict(int)
        self.freq_cnt = defaultdict(int)

    def add(self, number: int) -> None:
        prev_frq = self.num_to_freq[number]
        self.freq_cnt[prev_frq] -= 1
        if self.freq_cnt[prev_frq] <= 0:
            del self.freq_cnt[prev_frq]

        self.num_to_freq[number] += 1
        new_freq = self.num_to_freq[number]
        self.freq_cnt[new_freq] += 1


    def deleteOne(self, number: int) -> None:
        if self.num_to_freq[number] == 0:
            return
        prev_frq = self.num_to_freq[number]
        self.freq_cnt[prev_frq] -= 1
        if self.freq_cnt[prev_frq] <= 0:
            del self.freq_cnt[prev_frq]

        self.num_to_freq[number] -= 1
        new_freq = self.num_to_freq[number]
        self.freq_cnt[new_freq] += 1


    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq_cnt:
            return True
        else:
            return False

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)