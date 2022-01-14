import random

# Game responds to guesses with a list of G, Y and R for Green (correct), Yellow (incorrect position), Red (letter not in word)
# enter a space for an automatic guess

externaldictionary = 'enable1.txt'

def generatedict(n):
    ndict = []
    with open(externaldictionary, 'r') as words:
        ndict = [word.strip() for word in words if len(word.strip())==n]
    return ndict

def check(guess, puzzle):
    reply = []
    for x in range(len(guess)):
        if guess[x] == puzzle[x]:
            reply.append('G')
        elif guess[x] in puzzle:
            reply.append('Y')
        else:
            reply.append('R')
    print(reply)
    return reply


def play(wordlength=5, guesses=6):
    ndict = generatedict(wordlength)
    puzzle = random.choice(ndict)
    #print(puzzle)
    guesscount = 0
    reply = ['']*guesses
    while guesscount < guesses:
        guess = input('Input guess ' + str(guesscount+1) + ':')
        if guess == ' ':
            guess = guesser(reply, ndict)
            print('guesser picks: ' + guess)
        if guess in ndict:
            reply[guesscount] = check(guess, puzzle)
            if reply[guesscount] == ['G']*wordlength:
                print('You Win!')
                return 1
            guesscount+=1
        else:
            print('Invalid word')        
    print('No more guesses! You lose. Solution was: ' + puzzle)
    return 0

def guesser(puzzle, ndict):
    return random.choice(ndict)

def largestword(dict):
    big = ''
    with open(dict, 'r') as words:
            for word in words:
                if len(word) > len(big):
                    big = word
    return len(big)

if __name__ == "__main__":    
    play()
