import string


class Solution:
    def generateTag(self, caption: str) -> str:
        caption = caption.strip(" ")
        caption_words = caption.split(sep=" ")

        ret = "#"

        if len(caption_words) > 0:
            ret += caption_words[0].lower()

        for word in caption_words[1:]:
            ret += word.title()

        ret2 = ret[0]
        for ch in ret[1:]:
            if ch in string.ascii_letters:
                ret2 += ch

        if len(ret2) > 100:
            return ret2[:100]
        else:
            return ret2

# class Solution:
#     def generateTag(self, caption: str) -> str:
#         words = caption.split()
#
#         tag = "#"
#         for i, word in enumerate(words):
#             word = word.lower()
#             if i > 0:
#                 word = word.capitalize()
#             tag += word
# 
#         return tag[:100]