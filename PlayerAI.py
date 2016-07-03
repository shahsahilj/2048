#!/usr/bin/env python
#coding:utf-8

import sys
from random import randint
from BaseAI import BaseAI
import Minimax
import Minimaxab
from Grid import Grid
import numpy as np
import Helper

class PlayerAI(BaseAI):
        def getMove(self, grid):
                mapgrid = []
                for i in range(4):
                        mapgrid.extend(grid.map[i])
                [children,moving] = Helper.getAvailableChildren(mapgrid)
                maxpath = -np.inf
                direction = 0
                print len(children),len(moving)
                for i in range(len(children)):
                        c = children[i]
                        emptyTiles = len([j for j, x in enumerate(c) if x == 0])
                        m = moving[i]
                        highest_value = -np.inf
                        selection = 2
##                        if selection == '1':
##                            maxdepth = 4
##                            highest_value = Minimax.calculate(c, maxdepth, False)
##                            if m == 0 or m == 2:
##                                highest_value += 10000
                        if selection == 2:
                            maxdepth = 4
                            highest_value = Minimaxab.calculate(c, maxdepth,-np.inf,np.inf, False)
                            if m == 0 or m == 2:
                                highest_value += 10000
                            print highest_value,c,m
                        if highest_value > maxpath:
                            direction = m
                            maxpath = highest_value
##                return int(raw_input())
                return direction

if __name__ == '__main__':
        player = PlayerAI()
        g=Grid()
        g.map[0][0] = 2
        g.map[1][0] = 2
        g.map[3][0] = 4
        while True:
                for i in g.map:
                        print i
                print g.getAvailableMoves()
                v = player.getMove(g)
                g.move(v)



