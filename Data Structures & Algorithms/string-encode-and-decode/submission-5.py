class Solution:

    def encode(self, strs: List[str]) -> str:
        total_str = ""

        for s in strs:
            total_str += str(len(s)) + "#" + s
        
        return total_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        word_len = 0
        skip_until = -1

        for i in range(len(s)):
            if i <= skip_until:
                continue

            if s[i].isdigit() and i+1 < len(s):
                if s[i+1] == "#":
                    word_len = int(s[i])
                elif i+2 < len(s) and s[i+2] == "#":
                    word_len = int(s[i]+s[i+1])
                    skip_until = i + 1
                elif i+3 < len(s) and s[i+3] == "#":
                    word_len = int(s[i]+s[i+1]+s[i+2])
                    skip_until = i + 2

            if s[i] == "#":
                word = s[i+1:i+word_len+1]
                decoded_str.append(word)
                skip_until = i + word_len

        return decoded_str
