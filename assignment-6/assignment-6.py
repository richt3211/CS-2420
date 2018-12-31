from graphics import *
import math

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


def main():

    userFunction = input("Enter your function here and this program will draw it: ")
    userFunction = infixToPostFix(userFunction)
    print (userFunction)
    win = GraphWin("My Circle", 500, 500)
    XLOW = -10
    YLOW = -10
    XHIGH = +10
    YHIGH = +10
    win.setCoords(XLOW, YLOW,  XHIGH, YHIGH)
    #ratio = (wx- -10)/(20)
    #px = ratio * 500

    # Gather the x and y points
    xpoints = []
    ypoints = []
    x = XLOW
    while x<=XHIGH:
        y = evaluatePostFix(userFunction, x) 
        print (y)
        xpoints.append(x)
        ypoints.append(y)
        x += .1

    # Draw the x and y points
    for i in range(len(xpoints)-1):
        p1 = Point(xpoints[i], ypoints[i])
        p2 = Point(xpoints[i+1], ypoints[i+1])
        line = Line(p1, p2)
        line.draw(win)
        
    # x-axis
    linex = Line(Point(XLOW, 0), Point(XHIGH,0))
    linex.setOutline("red")
    linex.setWidth(3)
    linex.draw(win)
    # y-axis
    liney = Line(Point(0,YLOW), Point(0, YHIGH))
    liney.setOutline("red")
    liney.setWidth(3)
    liney.draw(win)
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

def infixToPostFix(input):
    stack = Stack()             #Initialize the operator stack
    postFix = ""                #Make output, which just HAS to start with a space
    for x in input:             #Loop over input
        if x in "0123456789x":  #if character is a number or a variable
            postFix += x        #then add it to the output
        elif x =="(":           #Otherwise, if the character is the beginning of a paranthesis,
            stack.push(x)       #then add it to the operator stack
        elif x == ")":          #If the character is the end of a stack,
            while stack.empty() == False:   #then loop through the stack
                top = stack.top()           #Cache the top character
                if top in "+-/*":           #if the top character is an operator besides the left parenthesis,
                    postFix += stack.pop()  #pop the operator to the postfix output
                elif top == "(":            #otherwise if the top character is a left parenthesis
                    stack.pop()             #then get rid of the top parenthesis
                    break                   #end of the parenthesis pair reached, so leave the loop
        elif x in "+-":         #if the character is a plus or a minus,
            top = stack.top()   #cache the top character
            if stack.empty() or top == "(":
                stack.push(x)
            else:
                postFix += stack.pop()
                stack.push(x)
        elif x in "*/":
            top = stack.top()
            if stack.empty() or top not in "*/" :
                stack.push(x)
            else:
                postFix += stack.pop()
                stack.push(x)
        # print ("Postfix: ",postFix)
        # print ("Stack: ",stack.mItems)
    while not stack.empty():
        postFix+= stack.pop()
    return postFix
def evaluatePostFix(input, value):
    stack = Stack()
    for x in input:
        if x in "x0123456789":
            if x =="x":
                stack.push(value)
            else:
                stack.push(float(x))
        elif x =="+":
            rhs = stack.pop()
            lhs = stack.pop ()
            number = lhs + rhs
            stack.push(number)
        elif x =="-":
            rhs = stack.pop()
            lhs = stack.pop()
            number = lhs - rhs
            stack.push(number)
        elif x =="/":
            rhs = stack.pop()
            lhs = stack.pop()
            number = lhs / rhs
            stack.push(number)
        elif x =="*":
            rhs = stack.pop()
            lhs = stack.pop()
            number = lhs * rhs
            stack.push(number)
    return stack.top()

if __name__ == "__main__":
    main()