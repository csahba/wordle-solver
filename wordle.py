from pickletools import read_bytes1
import random

externaldictionary = 'words_alpha.txt'

def generatedict(n):
    #return ['abc', 'abb', 'acc', 'add', 'bde', 'bba']
    ndict = []
    with open(externaldictionary, 'r') as words:
        ndict = [word.strip() for word in words if len(word.strip())==n]
            # if len(word) == n:
            #     worddict.append(word)
    return ndict

def check(guess, puzzle):
    if guess == puzzle:
        return True
    for x in range(len(guess)):
        if guess[x] == puzzle[x]:
            print('G ')
        elif guess[x] in puzzle:
            print('Y ')
        else:
            print('R ')
    return False


def play(wordlength=5, guesses=6):
    # while True:
    #     wordlength = input('Input game word length:')
    #     if wordlength in (range(1,largestword(externaldictionary)+1)):
    #         break
    ndict = generatedict(wordlength)
    puzzle = random.choice(ndict)
    print(puzzle)
    guesscount = 1
    while guesscount < guesses+1:
        guess = input('Input guess' + str(guesscount) + ':')
        if guess in ndict:
            guesscount+=1
            if check(guess, puzzle):
                print('You Win')
                return 1
        else:
            'Invalid word'
        
    print('No more guesses! You lose')
    return 0

def solve(puzzle, ndict):
    return

def largestword(dict):
    big = ''
    with open(dict, 'r') as words:
            for word in words:
                if len(word) > len(big):
                    big = word
    return len(big)

if __name__ == "__main__":    

    play()
