from typing import List
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        domain_to_count = defaultdict(int)
        for cpdomain in cpdomains:
            split_cpdomain = cpdomain.split()
            cnt = int(split_cpdomain[0])
            domain = split_cpdomain[1]
            domain_to_count[domain] += cnt

            next_start = domain.find('.') + 1

            while next_start:
                domain_to_count[domain[next_start:]] += cnt
                next_start = domain.find('.', next_start) + 1

        return [str(v) + " " + k for k, v in domain_to_count.items()]
