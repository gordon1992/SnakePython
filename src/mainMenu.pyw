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
    from tkinter.messagebox import showerror
except ImportError:
    # Python 2.x
    from Tkinter import *  # @UnusedWildImport
    from tkMessageBox import showerror
from snakeI import start as snakeI
from snakeII import start as snakeII
from string import punctuation
from sys import exit


class createWindow:

    def checkSnakeI():  # @NoSelf
        # Obtain user name from entry box and check to see if it's valid
        # (user name cannot contain punctuation)
        userName = entryUserName.get()
        for char in userName:
            if char in punctuation:
                showerror("Error - Invalid User name", \
                "Your user name is invalid. It can not contain these " \
                + "characters:\n" + str(punctuation))
                userName = ""
                return
        speed = ""
        if v.get() == 1:
            speed = "Slug"
        elif v.get() == 2:
            speed = "Worm"
        elif v.get() == 3:
            speed = "Python"
        if speed != "" and userName != "":
            snakeI(speed, userName)

    def checkSnakeII():  # @NoSelf
        # Obtain user name from entry box and check to see if it's valid
        # (user name cannot contain punctuation)
        userName = entryUserName.get()
        for char in userName:
            if char in punctuation:
                showerror("Error - Invalid User name", \
                "Your user name is invalid. It can not contain these " \
                + "characters:\n" + str(punctuation))
                userName = ""
                return
        speed = ""
        if v.get() == 1:
            speed = "Slug"
        elif v.get() == 2:
            speed = "Worm"
        elif v.get() == 3:
            speed = "Python"
        if speed != "" and userName != "":
            snakeII(speed, userName)

    # Define details for the window (size and menu options).
    root = Tk()
    root.title('Snake Clone - Main Menu')
    root.minsize(800, 500)
    root.maxsize(800, 500)
    root.geometry = root.minsize
    root.resizable(0, 0)

    # Define the fonts to use
    titleFont = "Calibri", 16
    menuFont = "Calibri", 12
    otherFont = "Calibri", 14

    # Create a top level menu
    menubar = Menu(root)
    menubar.add_command(label="Snake I", command=checkSnakeI, \
                        font=menuFont)
    menubar.add_command(label="Snake II", command=checkSnakeII, \
                        font=menuFont)
    menubar.add_command(label="Quit", command=exit, font=menuFont)
    root.config(menu=menubar)

    # Add title and instructions
    Label(text='Snake Clone', font=titleFont).pack(pady=15)
    instructions = "Instructions: \n Please use the arrow keys or WASD to " \
    + "move your snake to the food. Snake I and II are currently available. " \
    + "Each version should partly (if not very closely) resemble the " \
    + "official release.\nBefore playing please fill in the information "\
    + "below.\n"
    Label(text=instructions, wraplength=700, font=otherFont) .pack()

    # User name entry label
    textFrame = Frame(root)
    entryUserNameLabel = Label(textFrame)
    entryUserNameLabel["text"] = "Please enter your name:"
    entryUserNameLabel["font"] = otherFont
    entryUserNameLabel.pack(side=LEFT)
    textFrame.pack()

    global entryUserName, v

    # User name entry box
    entryUserName = Entry(textFrame)
    entryUserName['width'] = 50
    entryUserName.pack(side=RIGHT)

    # Computer difficulty radio buttons label
    anotherTextFrame = Frame(root)
    radioButtonsLabel = Label(anotherTextFrame)
    radioButtonsLabel["text"] = "\nPlease select one of the options below:"
    radioButtonsLabel["font"] = otherFont
    radioButtonsLabel.pack(side=BOTTOM)
    anotherTextFrame.pack()

    # Computer difficulty radio buttons
    v = IntVar()
    Radiobutton(root, text="Slug", variable=v, value=1, \
            font=otherFont).pack()
    Radiobutton(root, text="Worm", variable=v, value=2, \
            font=otherFont).pack()
    Radiobutton(root, text="Python", variable=v, value=3, \
            font=otherFont).pack()

    root.mainloop()
