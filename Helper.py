import math

def getAvailableChildren(grid):
    #gets all children and the moving directions
    allmoves = [0,1,2,3]
    children = []
    moving = []
    for m in allmoves:
        gridcopy = list(grid)
        moved = move(gridcopy, m)
        #move method returns True if moved and makes the change to gridcopy itself
        if moved == True:
            children.append(gridcopy)
            moving.append(m)
    return [children,moving]
def merge(cells):
    #merges the cells and sends back in order to be inserted
    if len(cells) <= 1:
        return cells
    i = 0
    while i < len(cells)-1:
        if cells[i] == cells[i+1]:
            cells[i] *= 2
            del cells[i+1]
        i += 1
def move(grid, direction):
    #if there is a move it is changed and return is True
    moved = False
    if direction == 0:
        #UP
        for i in range(4):
            cells = []
            #cells has all elements for a column from top to bottom
            for j in range(i,i+13,4):
                cell = grid[j]
                if cell != 0:
                    cells.append(cell)
            merge(cells)
            for j in range(i,i+13,4):
                value = cells.pop(0) if cells else 0
                if grid[j] != value:
                    moved = True
                grid[j] = value
        return moved
    elif direction == 1:
        #DOWN
        for i in range(4):
            cells = []
            #cells has all elements of column from bottom to top
            for j in range(i+12,i-1,-4):
                cell = grid[j]
                if cell != 0:
                    cells.append(cell)
            merge(cells)
            for j in range(i+12,i-1,-4):
                value = cells.pop(0) if cells else 0
                if grid[j] != value:
                    moved = True
                grid[j] = value
        return moved
    elif direction == 2:
        #LEFT
        for i in [0,4,8,12]:
            cells = []
            #cells has all elements of a row from left to right
            for j in range(i,i+4):
                cell = grid[j]
                if cell != 0:
                    cells.append(cell)
            merge(cells)
            for j in range(i,i+4):
                value = cells.pop(0) if cells else 0
                if grid[j] != value:
                    moved = True
                grid[j] = value
        return moved
    elif direction == 3:
        #RIGHT
        for i in [3,7,11,15]:
            cells = []
            #cells has all elements of a row from right to left
            for j in range(i,i-4,-1):
                cell = grid[j]
                if cell != 0:
                    cells.append(cell)
            merge(cells)
            for j in range(i,i-4,-1):
                value = cells.pop(0) if cells else 0
                if grid[j] != value:
                    moved = True
                grid[j] = value
        return moved
def canMove(grid):
    if 0 in grid:
        #if there is an empty space in the grid
        return True
    for i in range(16):
        if (i+1)%4!=0:
            #for all elements except the last column
            #if any element has same right element
            if grid[i]==grid[i+1]:
                return True
        if i<12:
            #for all except last row elements
            #if any element has same below element
            if grid[i]==grid[i+4]:
                return True
    return False

def CalcMerge(i,a,weights,MergeBonus):
    MergeBonus += (math.log(a)/math.log(2))*weights[i]*a
    return MergeBonus

def CalcOrder(i,a,weights,OrderBonus):
    OrderBonus += (math.log(a)/math.log(2))*weights[i]
    return OrderBonus


def heuristic(grid):
    #Try to keep largest tile in top left and others in decreasing order from left to right
    emptyTiles = len([i for i, x in enumerate(grid) if x == 0])
    maxTile = max(grid)
    MergeBonus = 0
    OrderBonus = 0
    Ord = 0
    penalty = 0
##    weights = [10,8,7,6.5,.5,.7,1,3,-.5,-1.5,-1.8,-2,-3.8,-3.7,-3.5,-3]
    weights = [65536,32768,16384,8192,512,1024,2048,4096,256,128,64,32,2,4,8,16]
    if maxTile == grid[0]:
        Ord += (math.log(grid[0])/math.log(2))*weights[0]
    for i in xrange(16):
        if grid[i] >= 8:
            Ord += weights[i]*(math.log(grid[i])/math.log(2))
##        if i < 4 and grid[i] == 0 :
##            Ord -=weights[i]*(math.log(maxTile)/math.log(2))
    return Ord/(16-emptyTiles)

    orig_grid = [[0] * 4 for i in xrange(4)]
    k = 0
    for i in range(4):
        for j in range(4):
            orig_grid[i][j] = grid[k]
            k += 1
    sm = 0
    for i in range(4):
        for j in range(4):
            if orig_grid[i][j] != 0:
                val = math.log(orig_grid[i][j])/math.log(2)
                for k in range(3-j):
                    nextright = orig_grid[i][j+k+1]
                    if nextright != 0:
                        rightval = math.log(nextright)/math.log(2)
                        if rightval != val:
                            sm -= math.fabs(rightval - val)
                            break
                for k in range(3-i):
                    nextdown = orig_grid[i+k+1][j]
                    if nextdown != 0:
                        downval = math.log(nextdown)/math.log(2)
                        if downval != val:
                            sm -= math.fabs(downval - val)
                            break
    mn = 0
    up = 0
    down = 0
    left = 0
    right = 0
    for i in range(4):
        j = 0
        k = j+1
        while k < 4:
            if orig_grid[i][k] == 0:
                k += 1
            else:
                if orig_grid[i][j] == 0:
                    curr = 0
                else:
                    curr = math.log(orig_grid[i][j])/math.log(2)
                nextval = math.log(orig_grid[i][k])/math.log(2)
                if curr > nextval:
                    up += nextval - curr
                elif nextval > curr:
                    down += curr - nextval
            j = k
            k += 1
    for j in range(4):
        i = 0
        k = i+1
        while k < 4:
            if orig_grid[j][k] == 0:
                k += 1
            else:
                if orig_grid[j][i] == 0:
                    curr = 0
                else:
                    curr = math.log(orig_grid[j][i])/math.log(2)
                nextval = math.log(orig_grid[j][k])/math.log(2)
                if curr > nextval:
                    left += nextval - curr
                elif nextval > curr:
                    right += curr - nextval
            i = k
            k += 1
    nm = max(up,down) + max(left,right)
    return 0.1*sm+mn+math.log(maxTile)/math.log(2)+ emptyTiles
