#import lines
from tkinter import *
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor
import turtlefigures
import turtle

#------------------------------------------
# Add The Frame and its Geometry
#------------------------------------------
root = Tk()
root.title("Turtle Application")
root.geometry("785x750+300+300")
root.configure(background='#00ffcc')

#------------------MAKE THE INTERFACE---------------------

#------------------------------------------
# Add Title Label
#------------------------------------------
label = Label(root, text = "Turtle Generator", fg="#ac00e6", bg="#00ffcc", font="Ariel 20 bold")
label.grid(row=0, column=0, columnspan=2)

#------------------------------------------
# Construct Canvas Panel
#------------------------------------------
canvasPanel = LabelFrame(root, text ="Canvas Frame", width = 500, height = 500, font="Ariel 15 bold")
canvasPanel.grid(row = 1, column = 1, rowspan=2)

canvas = Canvas(canvasPanel, width = 500, height = 500)
canvas.grid(row = 0, column = 0)

#------------------------------------------
# Set Pen and Screen Parameters
#------------------------------------------
screen = turtle.TurtleScreen(canvas)
pen = turtle.RawTurtle(screen)
screen.bgcolor("white")
pen.color("black")
pen.shape("turtle")
pen.speed(0)
pen.width(1)

#------------------------------------------
# Construct Control Panel
#------------------------------------------
controlPanel = LabelFrame(root, text = "Control Panel", width = 400, height = 500, font="Ariel 15 bold")
controlPanel.grid(row = 1, column = 0, rowspan=2)

#------------------------------------------
# Construct Shape Information Panel
#------------------------------------------
infoPanel = LabelFrame(canvasPanel, text = "Fractal Information Panel", width = 500, height = 300, font="Ariel 15 bold")
infoPanel.grid(row = 1, column = 0)

infoStr=StringVar()
infoLabel = Label(infoPanel, text = " ", textvariable=infoStr, wraplength=350)
infoLabel.pack()

#-------------------------------
# Fractal Length Widget
#-------------------------------
lengthLabel = Label(controlPanel, text = "Length")
lengthLabel.grid(row = 0, column = 0)

lengthStr = StringVar()
lengthEntry = Entry(controlPanel, textvariable = lengthStr)
lengthEntry.config(width=15)
lengthEntry.grid(row = 0, column = 1)

#-------------------------------
# Fractal Order Widget
#-------------------------------
orderLabel = Label(controlPanel, text = " Order")
orderLabel.grid(row = 1, column = 0)

orderStr = StringVar()
orderEntry = Entry(controlPanel, textvariable = orderStr)
orderEntry.config(width=15)
orderEntry.grid(row = 1, column = 1)

#------------------------------------------
# Add a Dropdown List for Fractal Selection
#------------------------------------------
fractalLabel = Label(controlPanel, text = "Fractal")
fractalLabel.grid(row = 2, column = 0)

figureList = ["Binary Tree", "Dandelion", "Snowflake", "Antiflake","Fern", "S-Gasket", "S-Carpet", "Octahedron", "C-Curve","Pentagon Spaced", "Pentagon No Spacing","Circle"]
figureStr = StringVar()
figureOptionMenu = ttk.OptionMenu(controlPanel, figureStr, figureList[0], *figureList)
figureOptionMenu.config(width=11)
figureOptionMenu.grid(row = 2, column = 1, pady=20)
figureStr.set("Binary Tree")

#-------------------------------
# Pen Speed Slider Widget
#-------------------------------
def penSpeedF(self):
    if penSpeedBar != None:
        pen.speed(penSpeedBar.get())

penSpeedBar = StringVar()
penSpeedBar = Scale(controlPanel, from_= 0, to = 10, orient=HORIZONTAL, command=penSpeedF)
penSpeedBar.config(length=140)
penSpeedBar.set(0)
penSpeedBar.grid(row = 3, column = 1, rowspan=2)

penSpeedLabel = Label(controlPanel, text = "Pen Speed")
penSpeedLabel.grid(row = 3, column = 0, rowspan=2)

#-------------------------------
# Pen Width Slider Widget
#-------------------------------
def penWidthF(self):
    if penWidthBar != None:
        pen.width(penWidthBar.get())

penWidthBar = StringVar()
penWidthBar = Scale(controlPanel, from_= 1, to = 10, orient=HORIZONTAL, command=penWidthF)
penWidthBar.config(length=140)
penWidthBar.set(1)
penWidthBar.grid(row = 5, column = 1, rowspan=2)

penWidthLabel = Label(controlPanel, text = "Pen Width")
penWidthLabel.grid(row = 5, column = 0, rowspan=2)

#------------------------------------------
# Construct Turtle Shape Panel
#------------------------------------------
shapePanel = LabelFrame(controlPanel, text = "Turtle Shapes", width = 500, height = 300, font="Ariel")
shapePanel.grid(row = 7, column = 0,columnspan=2, pady=20)

def turtleF():
    #Clear drawing and reset turtle
    pen.shape("turtle")   
#end
turtleButton = Button(shapePanel, text = "Turtle", width = 10, height = 2, command = turtleF)
turtleButton.grid(row = 0, column = 0)

def arrowF():
    #Clear drawing and reset turtle
    pen.shape("arrow")   
#end
turtleButton = Button(shapePanel, text = "Arrow", width = 10, height = 2, command = arrowF)
turtleButton.grid(row = 0, column = 1)

def squareF():
    #Clear drawing and reset turtle
    pen.shape("square")   
#end
squareButton = Button(shapePanel, text = "Square", width = 10, height = 2, command = squareF)
squareButton.grid(row = 1, column = 0)

def triangleF():
    #Clear drawing and reset turtle
    pen.shape("triangle")   
#end
triangleButton = Button(shapePanel, text = "Triangle", width = 10, height = 2, command = triangleF)
triangleButton.grid(row = 1, column = 1)

def circleF():
    #Clear drawing and reset turtle
    pen.shape("circle")   
#end
circleButton = Button(shapePanel, text = "Circle", width = 10, height = 2, command = circleF)
circleButton.grid(row = 2, column = 0)

def classicF():
    #Clear drawing and reset turtle
    pen.shape("classic")   
#end
classicButton = Button(shapePanel, text = "Classic", width = 10, height = 2, command = classicF)
classicButton.grid(row = 2, column = 1)

#------------------------------------------
# Canvas Background Color Selector Function
#------------------------------------------
def bgColorF():
    bgcolor = askcolor()
    if bgcolor != None:
        screen.bgcolor(str(bgcolor)[-9:-2])
            
bgColorButton = Button(controlPanel, text = "Pick Canvas Color", width = 20, height = 2, command=bgColorF)
bgColorButton.grid(row = 9, column = 0, columnspan=2)

#-------------------------------
# Pen Color Selector Function
#-------------------------------
def penColorF():
    pencolor = askcolor()
    if pencolor != None:
        pen.color(str(pencolor)[-9:-2])
            
penColorButton = Button(controlPanel, text = "Pick Pen Color", width = 20, height = 2, command=penColorF)
penColorButton.grid(row = 8, column = 0, columnspan=2)

#-------------------------------
# Add a Draw Button
#-------------------------------
def drawF():
    #get order and length as an integer
    length = int(lengthStr.get())
    order = int(orderStr.get())
    
    #get the figure ID
    figure = figureStr.get()
    figureId = figureList.index(figure)

    #get order and length as an string
    lengthTextStr=str(lengthStr.get())
    orderTextStr=str(orderStr.get())

    #if check to see what to draw
    if figureId == 0:
        infoStr.set("This is a binary tree fractal. A binary tree fractal is defined recursively by symmetric binary branching. Each branch is directed 45 degrees off of its parent segment. Below are the parameters set for the above graphic:\nLength = %s\nOrder = %s" % (lengthTextStr, orderTextStr))
        #draw binary tree
        #move pen to a better position
        pen.up();pen.left(90);pen.backward(length);pen.down()
        # pen draws
        turtlefigures.tree(order, length, pen)
        
    elif figureId == 1:
        infoStr.set("This is a dandelion fractal. Similar to a binary tree fractal, the dandelion fractal is defined recursively by symmetric binary branching. Each of its 4 branches are 60 degrees off of eachother over a 180 degree span. Below are the parameters set for the above graphic:\nLength = %s\nOrder = %s" % (lengthTextStr, orderTextStr))
        #draw dandelion
        #move pen to a better position
        pen.up();pen.left(90);pen.backward(length);pen.down()
        # pen draws
        turtlefigures.dandelion(order, length, pen)

    elif figureId == 2:
        infoStr.set("This is a snowflake fractal. The snowflake is generated by applying the Koch pattern to the shape of an upside-down equilateral triangle which results in a snowflake pattern. The order specified by the user is applied to the 4 lengths of the Koch pattern. Below are the parameters set for the above graphic:\nLength = %s\nOrder = %s" % (lengthTextStr, orderTextStr))
        #draw snowflake
        #move pen to a better position
        pen.up();pen.backward(length/2);pen.left(90);pen.forward(length/2);pen.right(90);pen.down()
        # pen draws
        turtlefigures.flake(order, length, pen)

    elif figureId == 3:
        infoStr.set("This is a antiflake fractal. Similar to the snowflake fractal, the antiflake is generated by applying the Koch pattern to the shape of a right-way up equilateral triangle which results in an inverted snowflake pattern. The order specified by the user is applied to the 4 lengths of the Koch pattern. Below are the parameters set for the above graphic:\nLength = %s\nOrder = %s" % (lengthTextStr, orderTextStr))
        #draw antiflake
        #move pen to a better position
        pen.up();pen.backward(length/2);pen.right(90);pen.forward(length/2);pen.left(90);pen.down()
        # pen draws
        turtlefigures.antiflake(order, length, pen)

    elif figureId == 4:
        infoStr.set("This is a fern fractal. The fern fractal (also referred to as the the Barnsley fern) is constructed similarly to the binary tree and dandelion, drawn in linear fashion with recursion of branches at irregular angles. Below are the parameters set for the above graphic:\nLength = %s\nOrder = %s" % (lengthTextStr, orderTextStr))
        #draw fern
        #move pen to a better position
        pen.up();pen.backward((length*order)/2);pen.down()
        # pen draws
        turtlefigures.fern(order, length, pen)

    elif figureId == 5:
        infoStr.set("This is the Sierpiński's gasket fractal. The Sierpiński Gasket is a self-similar fractal. The gasket is an equilateral triangle with a length specified by the user. Dependent on the order value specified by the user, smaller equilateral triangles will be recursively added to its internal area. Below are the parameters set for the above graphic:\nLength = %s\nOrder = %s" % (lengthTextStr, orderTextStr))
        #draw sierpinski gasket
        #move pen to a better position
        pen.up();pen.backward(length/2);pen.right(90);pen.forward(length/2);pen.left(90);pen.down()
        # pen draws
        turtlefigures.sgasket(order, length, pen)

    elif figureId == 6:
        infoStr.set("This is the Sierpiński's carpet fractal. The Sierpiński carpet is a plane fractal which consists of squares stack 3 high and 3 wide to form the outline of a larger square. The recursion occurs within each of the small squares. Below are the parameters set for the above graphic:\nLength = %s\nOrder = %s" % (lengthTextStr, orderTextStr))
        #draw sierpinskis carpet
        #move pen to a better position
        pen.up();pen.backward(length/2);pen.right(90);pen.backward(length/2);pen.left(90);pen.down()
        # pen draws
        turtlefigures.scarpet(order, length, pen)

    elif figureId == 7:
        infoStr.set("This is an octahedron fractal. This is the first of my personal contributions to the selection of fractals. The octahedron is a complex fractal that is 3D in nature which posed a challenge in programming the turtle representation. An octahedron is an 8-sided 3D object with triangular faces and I am satisfied with its representation in 2D space. Below are the parameters set for the above graphic:\nLength = %s\nOrder = %s" % (lengthTextStr, orderTextStr))
        #draw octahedron
        #move pen to a better position
        pen.up();pen.backward(length/2);pen.right(90);pen.backward(length/2);pen.left(90);pen.down()
        # pen draws
        turtlefigures.octahedron(order, length, pen)

    elif figureId == 8:
        infoStr.set("This is a c-curve fractal. The C-curve (also referred to as the the Levy C-curve) is a self-similar fractal structure that is built using 90 degree angles.  Below are the parameters set for the above graphic:\nLength = %s\nOrder = %s" % (lengthTextStr, orderTextStr))
        #draw c-curve
        #move pen to a better position
        pen.up();pen.backward(length);pen.down()
        # pen draws 
        turtlefigures.c(order, length, pen)

    elif figureId == 9:
        infoStr.set("This is a pentagon fractal with spacing. The pentagon with spacing is a self-similar fractal which forms in similar fashion to the Sierpiński gasket fractal. However, the pentagon images are not flush against eachother. Below are the parameters set for the above graphic:\nLength = %s\nOrder = %s" % (lengthTextStr, orderTextStr))
        #draw pentagon with spacing
        #move pen to a better position
        pen.up();pen.left(90);pen.backward(length);pen.right(90);pen.backward(length/2);pen.down()
        # pen draws
        turtlefigures.pent(order, length, pen)

    elif figureId == 10:
        infoStr.set("This is a pentagon fractal without spacing between the shapes. Mirroring the above fractal, the pentagon without spacing is a self-similar fractal which forms in similar fashion to the Sierpiński gasket fractal. The pentagon images are now flush against eachother. Refer to the readme.txt for further details on the calculation. Below are the parameters set for the above graphic:\nLength = %s\nOrder = %s" % (lengthTextStr, orderTextStr))
        #draw pentagon without spacing
        #move pen to a better position
        pen.up();pen.left(90);pen.backward(length);pen.right(90);pen.backward(length/2);pen.down()
        # pen draws
        turtlefigures.pent0(order, length, pen)

    elif figureId == 11:
        infoStr.set("This is a circle fractal.This is my personal circle fractal. Within the parent circle the are 4 smaller circles that fit flush against eachother. The radius required for these circles we calculated using Rbig = Rsmall + sqrt(2). With this equation, I determined that the remaining spaces between these 4 circles could be occupied by even smaller circles with radius sprt(2). Below are the parameters set for the above graphic:\nLength = %s\nOrder = %s" % (lengthTextStr, orderTextStr))
        #draw circle
        #move pen to a better position
        pen.up();pen.right(90);pen.forward(length);pen.left(90);pen.down()
        # pen draws
        turtlefigures.circle(order, length, pen)
    #end

drawButton = Button(controlPanel, text = "Draw", width = 10, height = 3, highlightbackground="limegreen", fg="gray", font = "Ariel 15 bold", command = drawF)
drawButton.grid(row = 12, column = 0, pady=27)

def hoverOnF(e):
    drawButton.config(fg="black", font = "Ariel 15 bold underline")
def hoverOffF(e):
    drawButton.config(fg="gray", font = "Ariel 15 bold")

drawButton.bind('<Enter>', hoverOnF)
drawButton.bind('<Leave>', hoverOffF)

#-------------------------------
# Add a Reset Button
#-------------------------------
def resetF():
    #Clear drawing and reset turtle
    pen.reset()
    lengthStr.set("")
    orderStr.set("")
    infoStr.set("")
    screen.bgcolor("white")
    pen.speed(0)
    pen.width(1)
    penWidthBar.set(1)
    penSpeedBar.set(0)
    
#end
resetButton = Button(controlPanel, text = "Reset", width = 10, height = 3, highlightbackground="red", fg = "gray", font = "Ariel 15 bold", command = resetF)
resetButton.grid(row = 12, column = 1, pady=27)

def hoverOnF(e):
    resetButton.config(fg="black", font = "Ariel 15 bold underline")
def hoverOffF(e):
    resetButton.config(fg="gray", font = "Ariel 15 bold")

resetButton.bind('<Enter>', hoverOnF)
resetButton.bind('<Leave>', hoverOffF)
