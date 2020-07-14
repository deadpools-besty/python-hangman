class Node:
    def __init__(self, initData, initNext):
        """ Constructs a new node and initializes it to contain
        the given object (initData) and link to the given next node. """
        
        self.data = initData
        self.next = initNext
        self.display = False

    def getData(self):
        """ Returns the element """
        return self.data

    def getNext(self):
        """ Returns the next node """
        return self.next

    def getDisplay(self):     
        return self.display

    def setData(self, newData):
        """ Sets newData as the element """
        self.data = newData

    def setNext(self, newNext):
        """ Sets newNext as the next node """
        self.next = newNext

    def setDisplay(self, newDisplay):
        self.display = newDisplay