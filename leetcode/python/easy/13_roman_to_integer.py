class Solution:
    LETTER_LIST = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    VALUE_LIST = [1, 5, 10, 50, 100, 500, 1000]

    def romanToInt(self, s: str) -> int:
        return self.parse_tokens(self.tokenize(s))

    def tokenize(self, s):
        tokens = []
        tmp_token = ''
        for c_i, c in enumerate(s):
            if c_i + 1 < len(s):
                idx = self.LETTER_LIST.index(c)
                n_idx = self.LETTER_LIST.index(s[c_i + 1])
                if n_idx > idx:
                    tmp_token += c
                    continue

            if not tmp_token:
                tokens.append(c)
            else:
                tokens.append(tmp_token + c)
                tmp_token = ''
        return tokens

    def parse_tokens(self, tokens):
        values = 0
        for t in tokens:
            if len(t) >= 2:
                values += self.VALUE_LIST[self.LETTER_LIST.index(t[1])] - self.VALUE_LIST[self.LETTER_LIST.index(t[0])]
            else:
                values += self.VALUE_LIST[self.LETTER_LIST.index(t)]
        return values


if __name__ == '__main__':
    s = Solution()

    print(s.romanToInt('III'))
    print(s.romanToInt('LVIII'))
    print(s.romanToInt('MCMXCIV'))
