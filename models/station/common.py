
RUN = 1
OPEN = 2
CLOSE = 3
state_str = {RUN: "running", OPEN: "opening", CLOSE: "closing"}


UP = 1
UPRIGHT = 2
RIGHT = 3
RIGHTDOWN = 4
DOWN = 5
DOWNLEFT = 6
LEFT = 7
LEFTUP = 8

COLORS = {5: 'red', 4: 'yellow', 2: 'orange', 1: 'green', 3: '#479AC7'}
def getDirection(source, target):
    deltaX, deltaY = target[0] - source[0], target[1] - source[1]
    if deltaX > 0 and deltaY > 0:
        return RIGHTDOWN
    elif deltaX > 0 and deltaY == 0:
        return RIGHT
    elif deltaX > 0 and deltaY < 0:
        return UPRIGHT
    elif deltaX == 0 and deltaY < 0:
        return UP
    elif deltaX == 0 and deltaY > 0:
        return DOWN
    elif deltaX < 0 and deltaY > 0:
        return DOWNLEFT
    elif deltaX < 0 and deltaY == 0:
        return LEFT
    elif deltaX < 0 and deltaY < 0:
        return LEFTUP
