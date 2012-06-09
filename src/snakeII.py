'''
    Snake Clone - Python implementation of the classic snake game.
    Copyright (C) 2012  Gordon Reid

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    The author can be contacted via email:
    gordon.reid1992@hotmail.co.uk
    OR
    1002536r@student.gla.ac.uk
'''


try:
    # Python 3.x
    from tkinter import *  # @UnusedWildImport
except ImportError:
    # Python 2.x
    from Tkinter import *  # @UnusedWildImport
from random import randrange


xMin = 10
yMin = 10
xMax = 490
yMax = 490


class snake():
    # Snake head object
    def __init__(self):
        self.diameter = 20
        self.colour = "red"
        self.speed = self.diameter
        self.length = 2
        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False
        self.score = 0
        self.headXPos = 250
        self.headYPos = 250
        self.tailXPos = 230
        self.tailYPos = 250
        self.gameOver = False
        self.stopTooQuickKeys = False


class food():
    # Food object created in random position in game area.
    def __init__(self):
        self.diameter = 20
        self.xPos = randrange(10, 490, 20)
        self.yPos = randrange(10, 490, 20)
        self.colour = "blue"
        self.timer = 1.0


def callback(event):
    key = event.keysym
    # Make snake move appropriately based on which key was pressed.
    # Only allow moving left if snake isn't moving right, only allow moving up
    # if snake isn't moving down etc...
    if (key == "Left" or key == "a") and not player.moveRight \
                            and not player.stopTooQuickKeys:
        player.moveLeft = True
        player.moveRight = False
        player.moveUp = False
        player.moveDown = False
        player.stopTooQuickKeys = True

    if (key == "Right" or key == "d") and not player.moveLeft \
                            and not player.stopTooQuickKeys:
        player.moveLeft = False
        player.moveRight = True
        player.moveUp = False
        player.moveDown = False
        player.stopTooQuickKeys = True

    if (key == "Up" or key == "w") and not player.moveDown \
                            and not player.stopTooQuickKeys:
        player.moveLeft = False
        player.moveRight = False
        player.moveUp = True
        player.moveDown = False
        player.stopTooQuickKeys = True

    if (key == "Down" or key == "s") and not player.moveUp \
                            and not player.stopTooQuickKeys:
        player.moveLeft = False
        player.moveRight = False
        player.moveUp = False
        player.moveDown = True
        player.stopTooQuickKeys = True


def makeBody(player, previousPositions, number, canvas):
        # Obtain appropriate coordinates for body piece.
        xPos = previousPositions[len(previousPositions) - number - 2][0]
        yPos = previousPositions[len(previousPositions) - number - 2][1]
        return canvas.create_oval(xPos, yPos, \
                xPos + player.diameter, yPos + \
                player.diameter, fill=player.colour)


def createMiniMap(canvas, element):
    startX = int(element[0] / 5) + 500
    startY = int(element[1] / 5) + 10
    return canvas.create_rectangle(startX, startY, startX + 2, \
                                    startY + 2, fill="black")


def play(canvas, mainGameWindow, speed, userName):
    # Initiate initial lists
    # Contains previous positions of player head [xPos, yPos]
    previousPositions = [[250, 250], [230, 250]]
    # Contains variable names for canvas body drawings.
    bodyList = []
    minimap = []
    x1 = int(xMin / 5) + 500
    x2 = int(xMax / 5) + 500
    y1 = int(yMin / 5) + 10
    y2 = int(yMax / 5) + 10
    canvas.create_rectangle(x1, y1, x2, y2)
    # Mazes [x1, y1, x2, y2] - same as canvas.create_X
    # x2 must be more than x1
    # y2 must be more than y1
    mazes = [[[0, 0, 0, 0], [0, 0, 0, 0]], \
            [[90, 90, 110, 410], [390, 90, 410, 410]], \
            [[90, 90, 390, 110], [90, 390, 390, 410]], \
            [[90, 90, 130, 130], [370, 90, 410, 130], \
            [370, 370, 410, 410], [90, 370, 130, 410]]]
    whichMaze = randrange(0, len(mazes))

    global player
    player = snake()
    someFood = food()

    if speed == "Slug":
        player.wait = int(1000 / 5)
    elif speed == "Worm":
        player.wait = int(1000 / 10)
    elif speed == "Python":
        player.wait = int(1000 / 20)

    player.userName = userName

    # Ensure food isn't overlapping a maze.
    for element in mazes[whichMaze]:
        while (someFood.xPos == player.headXPos and \
            someFood.yPos == player.headYPos) or \
            ([someFood.xPos, someFood.yPos] in previousPositions) or \
            (someFood.xPos in range(element[0], element[2]) and \
                    someFood.yPos in range(element[1], element[3])):
            someFood.xPos = randrange(10, 490, 20)
            someFood.yPos = randrange(10, 490, 20)
    massiveFont = "Calibri", 200

    # Three second countdown before game begins.
    for number in range(3):
        counter = canvas.create_text(250, 250, text=str(3 - number), \
                    font=massiveFont, fill="black")
        canvas.update()
        canvas.after(1000)
        canvas.delete(counter)

    for element in mazes[whichMaze]:
        canvas.create_rectangle(element[0], element[1], \
                                element[2], element[3], fill="black")
        x1 = int(element[0] / 5) + 500
        x2 = int(element[2] / 5) + 500
        y1 = int(element[1] / 5) + 10
        y2 = int(element[3] / 5) + 10
        if x1 > 500:
            canvas.create_rectangle(x1, y1, x2, y2, fill="black")
    if whichMaze == 1:
        player.moveUp = True
    else:
        player.moveRight = True

    imageFood = canvas.create_oval(someFood.xPos, someFood.yPos, \
                someFood.xPos + someFood.diameter, someFood.yPos + \
                someFood.diameter, fill=someFood.colour)
    head = canvas.create_oval(player.headXPos, player.headYPos, \
                player.headXPos + player.diameter, player.headYPos + \
                player.diameter, fill=player.colour)
    tail = canvas.create_oval(player.tailXPos, player.tailYPos, \
                player.tailXPos + player.diameter, player.tailYPos + \
                player.diameter, fill=player.colour)
    score = canvas.create_text(600, 200, text=("Score " + str(player.score)))

    # Continuous loop but broken out of when collision detected.
    while True:
        if player.moveLeft:
            player.headXPos -= player.speed
        elif player.moveRight:
            player.headXPos += player.speed
        elif player.moveUp:
            player.headYPos -= player.speed
        elif player.moveDown:
            player.headYPos += player.speed
        player.stopTooQuickKeys = False

        # Add the head's position to the start of the list and delete any
        # elements at the end if there are more elements than the length.
        previousPositions = [[player.headXPos, player.headYPos]] \
                            + previousPositions
        previousPositions = previousPositions[:player.length]

        # Tail's x and y are the coordinates at the end of the list.
        player.tailXPos = previousPositions[len(previousPositions) - 1][0]
        player.tailYPos = previousPositions[len(previousPositions) - 1][1]

        # If snake goes outside the game area, move it to the other side.
        if player.headXPos < xMin:
            player.headXPos = xMax - 20
            previousPositions[0][0] = xMax - 20
        if player.headXPos >= xMax:
            player.headXPos = xMin
            previousPositions[0][0] = xMin
        if player.headYPos < yMin:
            player.headYPos = yMax - 20
            previousPositions[0][1] = yMax - 20
        if player.headYPos >= yMax:
            player.headYPos = yMin
            previousPositions[0][1] = yMin

        # If snake's head is where the food is, eat the food, make snake bigger
        # and make new food.
        if player.headXPos == someFood.xPos and \
                player.headYPos == someFood.yPos:
            if player.wait == 200:
                player.score += int(someFood.timer * 90) + 10
            elif player.wait == 100:
                player.score += int(someFood.timer * 90) + 20
            elif player.wait == 50:
                player.score += int(someFood.timer * 90) + 30
            player.length += 1
            someFood = food()
            for element in mazes[whichMaze]:
                while (someFood.xPos == player.headXPos and \
            someFood.yPos == player.headYPos) or \
            ([someFood.xPos, someFood.yPos] in previousPositions) or \
            (someFood.xPos in range(element[0], element[2]) and \
            someFood.yPos in range(element[1], element[3])):
                    someFood.xPos = randrange(10, 490, 20)
                    someFood.yPos = randrange(10, 490, 20)

        # If snake overlaps itself, end the game.
        if ([player.headXPos, player.headYPos] in previousPositions[1:])\
        or (player.headXPos == player.tailXPos and \
        player.headYPos == player.tailYPos):
            player.gameOver = True

        # If player hits maze wall, end the game.
        for element in mazes[whichMaze]:
            if (player.headXPos in range(element[0], element[2]) and \
                    player.headYPos in range(element[1], element[3])):
                player.gameOver = True

        if player.gameOver:
            break

        # Delete every dynamic element then wait a certain interval
        for element in bodyList:
            canvas.delete(element)
        for element in minimap:
            canvas.delete(element)
        canvas.delete(head)
        canvas.delete(imageFood)
        canvas.delete(tail)
        canvas.delete(score)
        canvas.after(player.wait)
        someFood.timer = someFood.timer - (player.wait / 2500.0)
        if someFood.timer < 0:
            someFood.timer = 0

        imageFood = canvas.create_oval(someFood.xPos, someFood.yPos, \
                someFood.xPos + someFood.diameter, someFood.yPos + \
                someFood.diameter, fill=someFood.colour)
        head = canvas.create_oval(player.headXPos, player.headYPos, \
                player.headXPos + player.diameter, player.headYPos + \
                player.diameter, fill=player.colour)
        tail = canvas.create_oval(player.tailXPos, player.tailYPos, \
                player.tailXPos + player.diameter, player.tailYPos + \
                player.diameter, fill=player.colour)
        score = canvas.create_text(600, 200, text=("Score " \
                                                + str(player.score)))

        # Create mini map
        for element in previousPositions:
            minimap += [createMiniMap(canvas, element)]
        minimap += [createMiniMap(canvas, [someFood.xPos, someFood.yPos])]

        for number in range(player.length - 2):
            bodyList += [makeBody(player, previousPositions, number, canvas)]

        canvas.update()

    # Once game is over
    canvas.delete(score)
    canvas.create_text(600, 200, text=("Game over!\nCongratulations " + \
                        str(player.userName) + "\nYour final score is " + \
                        str(player.score)))
    canvas.update()
    canvas.after(3000)
    mainGameWindow.destroy()


def start(speed, userName):
    # Define details for the window (size and menu options).
    mainGameWindow = Toplevel(takefocus=True)
    mainGameWindow.title('Snake Clone - Snake II')
    mainGameWindow.minsize(700, 500)
    mainGameWindow.maxsize(700, 500)
    mainGameWindow.geometry = mainGameWindow.minsize
    mainGameWindow.resizable(0, 0)

    # Define details for the canvas widget which sits inside the
    # window (size and which function to call on key press).
    canvas = Canvas(mainGameWindow, width=700, height=500)
    canvas.bind_all('<Key>', callback)
    canvas.pack()
    canvas.create_rectangle(xMin, yMin, xMax, yMax, fill="white")
    play(canvas, mainGameWindow, speed, userName)
