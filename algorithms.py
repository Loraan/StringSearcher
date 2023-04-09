import timeit
from memory_profiler import memory_usage


class Searcher:
    def __init__(self, text, substring):
        self.text = text
        self.substring = substring

    def run(self):
        pass

    def test(self, loops_count=10):
        time = timeit.timeit('self.run()',
                             number=loops_count,
                             globals=locals()) / loops_count
        memory = memory_usage()[0]
        return time, memory

    def __str__(self):
        return f'Text: {self.text}\nSubstring: {self.substring}'


class BruteForce(Searcher):
    def run(self):
        i = j = 0
        text_len = len(self.text)
        substring_len = len(self.substring)
        while i <= text_len - substring_len and j < substring_len:
            if self.text[i + j] == self.substring[j]:
                j += 1
            else:
                i += 1
                j = 0
        return i if j == substring_len else -1

class KnuthMorrisPratt(Searcher):
    def run(self):
        index = -1
        text_len = len(self.text)
        substring_len = len(self.substring)
        prefix_table = [0] * text_len
        for i in range(1, text_len):
            k = prefix_table[i - 1]
            while k > 0 and self.text[k] != self.text[i]:
                k = prefix_table[k - 1]
            if self.text[k] == self.text[i]:
                k = k + 1
            prefix_table[i] = k
        k = 0
        for i in range(text_len):
            while k > 0 and self.substring[k] != self.text[i]:
                k = prefix_table[k - 1]
            if self.substring[k] == self.text[i]:
                k = k + 1
            if k == substring_len:
                index = i - substring_len + 1
                break
        return index

class RabinKarp(Searcher):
    def run(self):
        n, m = len(self.text), len(self.substring)
        hash_substring = hash(self.substring)
        for i in range(n - m + 1):
            hs = hash(self.text[i:i + m])
            if hs == hash_substring:
                if self.text[i:i + m] == self.substring:
                    return i
        return -1


class BoyerMoore(Searcher):
    def run(self):
        substring_len = len(self.substring)
        text_len = len(self.text)
        last_letter_occurences = [-1] * 2 ** 20
        for i in range(len(self.substring)):
            last_letter_occurences[ord(self.substring[i])] = i
        result = 0
        while result <= text_len - substring_len:
            j = substring_len - 1
            while j >= 0 and self.substring[j] == self.text[result + j]:
                j -= 1
            if j < 0:
                return result
            else:
                result += max(1, j - last_letter_occurences[ord(self.text[result + j])])
        return -1


class BoyerMooreHorspul(Searcher):
    def run(self):
        unique_symbols_substring = set()
        substring_len = len(self.substring)
        offsets_dict = {}
        for i in range(substring_len - 2, -1, -1):
            if self.substring[i] not in unique_symbols_substring:
                offsets_dict[self.substring[i]] = substring_len - i - 1
                unique_symbols_substring.add(self.substring[i])
        if self.substring[substring_len - 1] not in unique_symbols_substring:
            offsets_dict[self.substring[substring_len - 1]] = substring_len
        offsets_dict['*'] = substring_len
        text_len = len(self.text)
        if text_len >= substring_len:
            i = substring_len - 1
            while i < text_len:
                k = 0
                flBreak = False
                for j in range(substring_len - 1, -1, -1):
                    if self.text[i - k] != self.substring[j]:
                        if j == substring_len - 1:
                            if offsets_dict.get(self.text[i], False):
                                off = offsets_dict[self.text[i]]
                            else:
                                off = offsets_dict['*']
                        else:
                            off = offsets_dict[self.substring[j]]
                        i += off
                        flBreak = True
                        break
                    k += 1
                if not flBreak:
                    return i-k+1
            else:
                return -1
        else:
            return -1
