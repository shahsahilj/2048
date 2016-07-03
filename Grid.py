#/usr/bin/env python
#coding:utf-8
from sets import Set
from copy import deepcopy

# direction vectors
directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)

class Grid:
    def __init__(self, size = 4):
        self.size = size
        self.map = [[0] * self.size for i in xrange(self.size)]

    # make a deepcopy of this current object
    def clone(self):
        gridCopy = Grid()
        gridCopy.map = deepcopy(self.map)
        gridCopy.size = self.size
        return gridCopy

    # insert a tile in an empty cell
    def insertTile(self, pos, value):
        self.setCellValue(pos, value)

    def setCellValue(self, (x, y), value):
        self.map[x][y] = value

    # return all the empty cells
    def getAvailableCells(self):
        cells = []
        for x in xrange(self.size):
            for y in xrange(self.size):
                if self.map[x][y] == 0:
                    cells.append((x,y))
        return cells

    # return the tile with maximum number
    def getMaxTile(self):
        maxTile = 0
        for x in xrange(self.size):
            for y in xrange(self.size):
                maxTile = max(maxTile, self.map[x][y])
        return maxTile

    # check whether we can insert a tile in pos
    def canInsert(self, pos):
        return self.getCellValue(pos) == 0

    # move the grid
    def move(self, dir):
        dir = int(dir)
        if dir == UP:
            return self.moveUD(False)
        if dir == DOWN:
            return self.moveUD(True)
        if dir == LEFT:
            return self.moveLR(False)
        if dir == RIGHT:
            return self.moveLR(True)

    # move up or down
    def moveUD(self, down):
        r = range(self.size -1, -1, -1) if down else range(self.size)
        moved = False
        for j in range(self.size):
            cells = []
            for i in r:
                cell = self.map[i][j]
                if cell != 0:
                    cells.append(cell)
            self.merge(cells)
            for i in r:
                value = cells.pop(0) if cells else 0
                if self.map[i][j] != value:
                    moved = True
                self.map[i][j] = value
        return moved

    # move left or right
    def moveLR(self, right):
        r = range(self.size - 1, -1, -1) if right else range(self.size)
        moved = False
        for i in range(self.size):
            cells = []
            for j in r:
                cell = self.map[i][j]
                if cell != 0:
                    cells.append(cell)
            self.merge(cells)
            for j in r:
                value = cells.pop(0) if cells else 0
                if self.map[i][j] != value:
                    moved = True
                self.map[i][j] = value
        return moved

    # merge tiles
    def merge(self, cells):
        if len(cells) <= 1:
            return cells
        i = 0
        while i < len(cells) - 1:
            if cells[i] == cells[i+1]:
                cells[i] *= 2
                del cells[i+1]
            i += 1

    def canMove(self, dirs = vecIndex):
        # init moves to be checked
        checkingMoves = Set(dirs)

        for x in xrange(self.size):
            for y in xrange(self.size):
                # if current cell is filled
                if self.map[x][y]:
                    # look ajacent cell value
                    for i in checkingMoves:
                        move = directionVectors[i]
                        adjCellValue = self.getCellValue((x + move[0], y + move[1]))
                        # if value is the same or ajacent cell is empty
                        if adjCellValue == self.map[x][y] or adjCellValue == 0:
                            return True
                # else if current cell is emtpy
                elif self.map[x][y] == 0:
                    return True
        return False

    # return all vailable moves, can be optimized
    def getAvailableMoves(self, dirs = vecIndex):
        availableMoves = []
        for x in dirs:
            gridCopy = self.clone()
            if gridCopy.move(x):
                availableMoves.append(x)
        return availableMoves

    def crossBound(self, (x, y)):
        return x < 0 or x >= self.size or y < 0 or y >= self.size

    def getCellValue(self, pos):
        if not self.crossBound(pos):
            return self.map[pos[0]][pos[1]]
        else:
            return None

if __name__ == '__main__':
    g = Grid()
    g.map[0][0] = 2
    g.map[1][0] = 2
    g.map[3][0] = 4
    while True:
        for i in g.map:
            print i
        print g.getAvailableMoves()
        v = raw_input()
        g.move(v)
