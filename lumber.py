__author__ = "Sanket Agarwal"


"""

Author: Sanket Agarwal


Program to grow trees and then harvest them and pile them
in a sorted and unsorted way.
"""


import turtle
import yard
import random
def buttons(position):
    """
    Draw the two buttons for sorted and unsorted pile choices.
    :pre: (relative) pos (0,0), heading (North), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """
    turtle.penup()
    turtle.left(90)
    turtle.backward(position)
    turtle.pendown()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(340)
    turtle.left(90)
    turtle.fd(40)
    turtle.left(90)
    turtle.fd(340)
    turtle.fd(340)
    turtle.left(90)
    turtle.fd(40)
    turtle.left(90)
    turtle.forward(340)
    turtle.penup()
    turtle.left(180)
    turtle.backward(180)
    turtle.right(90)
    turtle.forward(20)
    turtle.pendown()
    turtle.write("Harvest and sort")
    turtle.penup()
    turtle.left(90)
    turtle.forward(340)
    turtle.pendown()
    turtle.write("Harvest unorted")
    turtle.penup()
    turtle.backward(160)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)


def drawTrunk(xcor,ycor):
    """
    Draws the  trunk of random length and the top of the trunk has
    always a distance of 50 pixels from top of the window.
    :pre: (relative) pos (0,0), heading (North), up
    :post: (relative) pos (0,0), heading (north), up
    :return: Length of the trunk.
    """
    turtle.penup()
    turtle.goto(xcor,ycor)
    turtle.pendown()
    turtle.setheading(90)
    turtle.pendown()
    trLength = random.randint(50,250)
    if ycor > 0 and (ycor + trLength) > 230:
        extraLength = (ycor + trLength) - 230
        trLength    = trLength - extraLength
        turtle.forward(trLength)
    else:
        turtle.forward(trLength)
    return trLength

def drawPine(x,y):
    """
    Draw the Pine tree ..
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    :return: Length of the trunk.
    """
    log = drawTrunk(x,y)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(30)
    turtle.penup()
    return log

def drawMaple(x,y):
    """
    Draw the Maple tree ..
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    :return: Length of the trunk.
    """
    log  = drawTrunk(x, y)
    turtle.right(90)
    turtle.circle(30)
    turtle.penup()
    return log

def drawSqTree(x,y):
    """
    Draw the Square  tree ..
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    :return: Length of the trunk.
    """
    log = drawTrunk(x, y)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(30)
    turtle.penup()
    return log

def logPiling(list):
    """
    Harvest the trees and pile them ..
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None.
    """
    sum = 0
    ht  = 10

    turtle.clear()
    turtle.home()
    for l in list:
        sum = sum + l
        turtle.pendown()
        turtle.forward(l/2)
        turtle.left(90)
        turtle.forward(ht)
        turtle.left(90)
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(ht)
        turtle.left(90)
        turtle.forward(l/2)
        turtle.penup()
        turtle.forward(l/2)
        turtle.left(90)
        turtle.forward(ht)
        turtle.left(90)
        turtle.forward(l/2)
        turtle.left(180)
    print("Total length of all the logs put together is:")
    print(sum)
    turtle.exitonclick()

    """
Creates the object of class LumberYard
    """
lObj = yard.LumberYard()
def doclick(x,y):
    """
    Handles the on click calls,
    the growing of trees and piling is done here.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None.
    """

    log = []
    l = 0
    if y > (-230) and y < 230:

        r = random.randint(1, 3)

        if r == 1:
          log =   drawMaple(x, y)

        elif r == 2:
          log = drawPine(x, y)

        elif r == 3:
          log = drawSqTree(x, y)

        yard.LumberYard.addLog(lObj, log)

    if x < 0:
        if y < -230 and y > -270:
            list = yard.LumberYard.allLogs(lObj)
            list.sort();
            list.reverse();
            logPiling(list)

    elif x > 0:
        if y < -230 and y > -270:
            list = yard.LumberYard.allLogs(lObj)
            logPiling(list)

def main():
    """
    The main function.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    turtle.screensize(400, 300)
    buttons(270)
    turtle.onscreenclick(fun=doclick)
    turtle.mainloop()

if __name__ == '__main__':
    main()




