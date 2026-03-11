from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # TODO: can also use binary search O(n*m^2)

        products.sort()  # lexicographical sort
        result = []
        prefix = ""
        filtered = products  # start with all products

        for char in searchWord:
            prefix += char
            # filter products that start with current prefix
            filtered = [p for p in filtered if p.startswith(prefix)]
            # take at most 3
            result.append(filtered[:3])

        return result
