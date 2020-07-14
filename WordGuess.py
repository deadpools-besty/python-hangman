import random
from SecretWord import SecretWord

class WordGuess:

    def __init__(self, wordDic):
        self.secretWord = SecretWord()
        self.wordDic = wordDic
        self.allotedGuesses = 0
        self.lettersGuessed = []

    def play(self):
        """ Plays out a single full game of Word Guess """
        self.chooseSecretWord()
        self.setGuessAmount()
        print('A secret word has been randomly chosen!')

        while not self.secretWord.isSolved() and self.allotedGuesses != 0:
            print('You have %d guesses remaining' %self.allotedGuesses)
            print('Word Guess Progress: %s' % self.secretWord.printProgress())
            self.getGuess()
        if self.secretWord.isSolved():
            print('You solved the puzzle!')
        print('The secret word was: %s' %self.secretWord.__str__())

    def chooseSecretWord(self):
        """ Chooses the secret word that will be guessed """
        randomWord = random.choice(list(self.wordDic.keys()))
        self.secretWord.setWord(randomWord)

    def editDistance(self, s1, s2):
        """ Recursively returns the total number of insertions and deletions required to convert S1 into S2 """
        s1 = s1.__str__()
        s2 = s2.__str__()
        
        if len(s1) == 0: # if s1 is empty, need to insert all the chars from s2
            return len(s2)
        if len(s2) == 0: # if s2 is empty, need to remove all the chars in s1
            return len(s1)
        if len(s1) == 0 and len(s2) == 0: # if both are empty, nothing to do
            return 0
        if s1[0] == s2[0]: # first letters are the same find edit distance of the smaller substring
            return self.editDistance(s1[1:], s2[1:])
        else:
            return min([self.editDistance(s1[1:], s2) + 1, self.editDistance(s1, s2[1:]) + 1]) 
        

    def setGuessAmount(self):
        dist = self.editDistance(self.secretWord, self.secretWord.sort())
        if dist in range(5,16):
            self.allotedGuesses = 2*dist
        elif dist < 5:
            self.allotedGuesses = 5
        elif dist > 15:
            self.allotedGuesses = 15
        
    
    def getGuess(self):
        """ Queries the user to guess a character in the secret word """


        usrGuess = input('Enter a character that has not been guessed or * for a hint: ')
        if usrGuess not in self.lettersGuessed and usrGuess != '*':
            self.secretWord.update(usrGuess)
            if usrGuess not in self.secretWord.__str__(): # decrement allotedGuesses if letter is not in word
                self.allotedGuesses -= 1
            self.lettersGuessed.append(usrGuess)
        elif usrGuess == '*':
            self.allotedGuesses -= 1
            print('Hint: %s' %self.wordDic[self.secretWord.__str__()])
        else:
            self.getGuess()
            
                
                
    
#w = WordGuess({'apple':'fruit', 'hockey':'sport'})
#w.chooseSecretWord()
#print(w.secretWord)
#print(w.editDistance(w.secretWord, w.secretWord.sort()))
#w.getGuess()
#w.getGuess()