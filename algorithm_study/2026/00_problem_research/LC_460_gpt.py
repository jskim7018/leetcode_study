from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val_freq = {}  # key -> (value, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> keys (LRU order)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1

        value, freq = self.key_to_val_freq[key]

        # remove from current freq
        del self.freq_to_keys[freq][key]

        # if this freq is now empty and was min_freq → update
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # add to next freq
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_val_freq[key] = (value, freq + 1)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            # update value + increase freq
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self.get(key)
            return

        # evict if needed
        if len(self.key_to_val_freq) >= self.capacity:
            # remove LRU from min_freq
            lru_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[lru_key]

            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

        # insert new key with freq = 1
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1