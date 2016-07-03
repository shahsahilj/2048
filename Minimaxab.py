import Helper
import numpy as np

def calculate(grid, maxdepth, alpha, beta, is_it_max):
    if maxdepth == 0:
        return Helper.heuristic(grid)
    if not Helper.canMove(grid):
        return Helper.heuristic(grid)
    if is_it_max:
        v = -np.inf
        [children, moving] = Helper.getAvailableChildren(grid)
        for child in children:
            v = max(v,calculate(child,maxdepth-1,alpha,beta,False))
            if v >= beta:
                return v
            alpha = max(alpha,v)
        return v
    else:
        cells = [i for i, x in enumerate(grid) if x == 0]
        children = []
        for c in cells:
            gridcopy = list(grid)
            gridcopy[c]=2
            children.append(gridcopy)
            gridcopy = list(grid)
            gridcopy[c]=4
            children.append(gridcopy)
        v = np.inf
        for child in children:
            v = min(v,calculate(child,maxdepth-1,alpha,beta,True))
            if v <= alpha:
                return v
            beta = min(beta,v)
        return v
