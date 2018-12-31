class Stack:

    def __init__(self):
        self.mItems = []
        self.mLength = 0
    def top(self):
        if self.empty() == False:
            return self.mItems[self.mLength -1]
    def push(self, item):
        self.mItems.append(item)
        self.mLength +=1
    def pop(self):
        if self.empty() == False:
            a = self.mItems.pop()
            self.mLength -=1
            return a
    def empty(self):
        if len(self.mItems) == 0:
            return True
        else:
            return False
