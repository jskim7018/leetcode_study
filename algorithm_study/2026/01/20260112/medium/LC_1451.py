class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text[0].lower() + text[1:]
        split_text = text.split()
        sorted_text = sorted(split_text, key=lambda t: len(t))

        sorted_text[0] = sorted_text[0].capitalize()

        return ' '.join(sorted_text)
