class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        is_neg = False
        if numerator < 0:
            is_neg = not is_neg
            numerator = -numerator
        if denominator < 0 and numerator != 0:
            is_neg = not is_neg
            denominator = -denominator

        curr_numerator = numerator

        numerator_visited = dict()

        integer_place = str(curr_numerator // denominator)
        curr_numerator = curr_numerator % denominator
        curr_numerator *= 10
        frag_place = []

        if curr_numerator > 0:
            frag_place.append('.')

        while curr_numerator > 0:
            if curr_numerator in numerator_visited:
                frag_place.insert(numerator_visited[curr_numerator], '(')
                frag_place.append(')')
                break
            numerator_visited[curr_numerator] = len(frag_place)

            next_div = curr_numerator // denominator
            frag_place.append(str(next_div))
            curr_numerator = curr_numerator % denominator
            curr_numerator *= 10
        ans_pos = integer_place + ''.join(frag_place)

        if is_neg:
            return '-' + ans_pos
        else:
            return ans_pos
