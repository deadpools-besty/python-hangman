'''input
2
foo
bar
'''

from WordGuess import WordGuess


def readWords(filename):
    """ Read in the list of possible secret words and their corresponding hints """
    try:
        f = open(filename, 'r')
        wordsDic = {}
        for line in f:
            lineList = line.strip('\n').split()
            wordsDic[lineList[0]] = lineList[1]
        f.close()
        return wordsDic
    except FileNotFoundError:
        print('Incorrect filename. Be sure to add .txt extension')

def main():
    
    playAgain = True
    filename = input('Please enter a Word Guess input file: ')
    wordsDict = readWords(filename)
    wordGame = WordGuess(wordsDict)
    wordGame.play()
    userChoice = input('Would you like to play again? (y/n): ')
    if userChoice == 'n':
        playAgain = False
    else:
        main()
         
if __name__ == "__main__":
    main()