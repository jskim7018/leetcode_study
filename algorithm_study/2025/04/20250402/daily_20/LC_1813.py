class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) >= len(sentence2):
            longer_sentence = sentence1
            shorter_sentence = sentence2
        else:
            shorter_sentence = sentence1
            longer_sentence = sentence2

        split_ls = longer_sentence.split(' ')
        split_ss = shorter_sentence.split(' ')


        left_pointer = 0
        right_pointer = 1

        while left_pointer < len(split_ss):
            if split_ss[left_pointer] != split_ls[left_pointer]:
                break
            else:
                left_pointer += 1
        while right_pointer <= len(split_ss):
            if split_ss[-right_pointer] != split_ls[-right_pointer]:
                break
            else:
                right_pointer += 1

        return len(split_ss) <= left_pointer+(right_pointer-1)
