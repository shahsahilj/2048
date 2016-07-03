import numpy as np
import Helper

def calculate(grid, maxdepth, is_it_max):
    if maxdepth == 0:
        return Helper.heuristic(grid)
    if not Helper.canMove(grid):
        return Helper.heuristic(grid)
    if is_it_max:
        v = -np.inf
        [children, moving] = Helper.getAvailableChildren(grid)
        for child in children:
            v = max(v,calculate(child,maxdepth-1,False))
        return v
    else:
        cells = [i for i, x in enumerate(grid) if x == 0]
        children = []
        v = np.inf
        for c in cells:
            gridcopy = list(grid)
            gridcopy[c]=2
            children.append(gridcopy)
            gridcopy = list(grid)
            gridcopy[c]=4
            children.append(gridcopy)
        for child in children:
            v = min(v,calculate(child,maxdepth-1,True))
        return v
