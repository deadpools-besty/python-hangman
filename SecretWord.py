from Node import Node
import copy

class LinkedList:
    """ The Singly-Linked List class defined in lecture """

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def length(self):
        return self.size

    def add(self, item):
        temp = Node(item, None)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1

    def insert(self, pos, item):
        
        temp = Node(item, None)
        current = self.head
        prev = None
        if pos == 0:
            self.add(item)          
        else:
            while current != None and self.index(current.getData()) != pos:
                prev = current
                current = current.getNext()
            if self.index(current.getData()) == pos:
                temp.setNext(current)
                prev.setNext(temp)
                self.size += 1
     
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def index (self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1

        if not found:
            index = -1

        return index

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        self.size -= 1

        return found

    def append(self, item):
        temp = Node(item, None)
        if self.head == None:
            self.head = temp
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)
        self.size += 1

    def pop(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()

        if previous == None:
            self.head = None
        else:
            previous.setNext(None)
        self.size -= 1
        return current.getData()

    def getHead(self):
        return self.head

class SecretWord:

    def __init__(self):
        self.linkedList = LinkedList()
        # Additional attribute(s) go here:


    def setWord(self, word):
        """ Adds the characters in 'word' to self.linkedList in the given order """
        while self.linkedList.length() > 0:
            self.linkedList.pop()
        for char in word:
            self.linkedList.append(char)

 
    def sort(self):
        """ Sorts the characters stored in self.linkedList in alphabetical order """
        
        sortedSecretWordObj = SecretWord()
        sortedList = sortedSecretWordObj.getLinkedList()
        current = self.linkedList.getHead().getNext()
        sortedList.add(self.linkedList.getHead().getData()) # add first item list
        while current != None and sortedList.length() < self.linkedList.length(): #go through each item in the linked list till it reaches the end or, the second one's length matches the first
            otherCurrent = sortedList.getHead()
            while otherCurrent.getNext() != None and ord(otherCurrent.getData()) < ord(current.getData()): # go through the each item in list till the next one is greater than the item to insert
                otherCurrent = otherCurrent.getNext()
            if otherCurrent.getNext() == None and ord(otherCurrent.getData()) < ord(current.getData()):
                sortedList.append(current.getData())
            else:
                sortedList.insert(sortedList.index(otherCurrent.getData()), current.getData())
            current = current.getNext()
 
        return sortedSecretWordObj
        
        
        
    def isSolved(self):
        """ Returns whether SecretWord has been solved (all letters in the word have been guessed by the user) """
        if self.printProgress() == self.__str__():
            return True  
        else:
            return False

    def update(self, guess):
        """ Updates the nodes in self.linkedList that match 'guess' """
        current = self.linkedList.getHead()
        while current != None:
            if current.getData() == guess:
                current.setDisplay(True)
            current = current.getNext()

    def printProgress(self):
        """ Prints the current game progress
        Ex: y _ l l _ w """
        current = self.linkedList.getHead()
        string = ''
        while current != None:
            if current.getDisplay() == False:
                string += '_ '
            else:
                string += current.getData()
            current = current.getNext()
        return string
        

    def getLinkedList(self):
        return self.linkedList
    
    def __str__(self):
        """ Converts the characters in self.linkedList into a string """
        word = ''
        current = self.linkedList.getHead()
        i = 0
        while i < self.linkedList.length():
            word = word + current.getData()
            current = current.getNext()
            i += 1
        return word