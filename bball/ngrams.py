import string


def main():
    words = Input()
    print(words.wordlist())
    

class Input:
    def __init__(self):
        self._file = open(input())

    def wordlist(self):
        wordlist = []
        for line in self._file:
            line = line.split()
            for word in line:
                word = word.strip(string.punctuation)
                if word != '':
                    wordlist.append(word)
        return wordlist


class Ngrams:
    def __init__(self):
        self._n = input()
        self._current = []

    def update(self, ngram):
        pass

    def process_wordlist(self, wordlist):
        for word in wordlist:
            M = 0
            if word == 0:
                pass
                

    def print_max_ngrams(self):
        print("{:d} -- {}".format(M, ngram_string))
            
                










main()
