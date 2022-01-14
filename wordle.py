import random


wordlength = 3
guessnumber = 5

def generatedict(n):
    #return ['abc', 'abb', 'acc', 'add', 'bde', 'bba']
    worddict = []
    with open('words_alpha.txt', 'r') as words:
        for word in words:
            if len(word) == n:
                worddict.append(word)
    return worddict

def solve(puzzle, ndict):
    return

ndict = generatedict(wordlength+1)
puzzle = random.choice(ndict)
print(puzzle)


