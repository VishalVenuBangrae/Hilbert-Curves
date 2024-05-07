from graphics import *
import sys

length = 32
x = 10
y = 10


def goEast(win):
    global x
    global y
    p1 = Point(x, y)
    x = x + length
    p2 = Point(x, y)
    line = Line(p1, p2)
    line.draw(win)


def goWest(win):
    global x
    global y
    p1 = Point(x, y)
    x = x - length
    p2 = Point(x, y)
    line = Line(p1, p2)
    line.draw(win)


def goNorth(win):
    global x
    global y
    p1 = Point(x, y)
    y = y - length
    p2 = Point(x, y)
    line = Line(p1, p2)
    line.draw(win)


def goSouth(win):
    global x
    global y
    p1 = Point(x, y)
    y = y + length
    p2 = Point(x, y)
    line = Line(p1, p2)
    line.draw(win)


def aCurve(size, win):
    if size > 0:
        hCurve(size - 1, win)
        goEast(win)
        aCurve(size - 1, win)
        goSouth(win)
        aCurve(size - 1, win)
        goWest(win)
        cCurve(size - 1, win)


def bCurve(size, win):
    if size > 0:
        cCurve(size - 1, win)
        goWest(win)
        bCurve(size - 1, win)
        goNorth(win)
        bCurve(size - 1, win)
        goEast(win)
        hCurve(size - 1, win)


def cCurve(size, win):
    if size > 0:
        bCurve(size - 1, win)
        goNorth(win)
        cCurve(size - 1, win)
        goWest(win)
        cCurve(size - 1, win)
        goSouth(win)
        aCurve(size - 1, win)


def hCurve(size, win):
    if size > 0:
        aCurve(size - 1, win)
        goSouth(win)
        hCurve(size - 1, win)
        goEast(win)
        hCurve(size - 1, win)
        goNorth(win)
        bCurve(size - 1, win)


win = GraphWin("Toothpick", 1000, 1000)
win.setBackground("white")
x = int(sys.argv[1])
hCurve(x, win)
win.getMouse()
win.close()
