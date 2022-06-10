from random import randint
from BaseAI import BaseAI
from pdb import set_trace
import time

timeLimit = 0.2

def h(grid):
    return hash(tuple([tuple(x) for x in grid.map]))
    
class PlayerAI(BaseAI):
    
    def getMove(self, grid):
        ''' 
            UP 0
            DOWN 1
            LEFT 2
            RIGHT 3
        '''
        self.startTime = time.clock()
        self.depthLimit = 6
        self.heuristics = dict()
        self.childrenMax = dict()
        self.childrenMin = dict()
        bestMove = None
        while not self.timeOver():
            move, _, _ = self.maximize(grid, float('-inf'), float('inf'), 1)
            self.depthLimit +=1
            if not self.timeOver() or bestMove is None:
                bestMove = move
        return bestMove
        
    def maximize(self, grid, alpha, beta, depth):
        if self.timeOver() or depth > self.depthLimit:
                return None, None, self.evaluation(grid)

        key = h(grid)
        if key not in self.childrenMax:
            moves = grid.getAvailableMoves()
            if not moves:
                return None, None, self.evaluation(grid)
            children = []
            for move in moves:
                child = grid.clone()
                child.move(move)
                children.append([child, move])
            self.childrenMax[key] = children
        maxChild, maxUtility = None, float('-inf')

        for child in self.childrenMax[key]:
            _, _, utility = self.minimize(child[0], alpha, beta, depth + 1)

            if utility > maxUtility:
                bestMove, maxChild, maxUtility = child[1], child[0], utility

            if maxUtility >= beta:
                break

            if maxUtility > alpha:
                alpha = maxUtility

        return bestMove, maxChild, maxUtility

    def minimize(self, grid, alpha, beta, depth):
        if self.timeOver() or depth > self.depthLimit:
            return None, None, self.evaluation(grid)

        key = h(grid)
        if key not in self.childrenMin:
            cells = grid.getAvailableCells()
            if not cells:
                return None, None, self.evaluation(grid)
            children = []
            for cell in cells:
                child = grid.clone()
                child.insertTile(cell, 2)
                children.append(child)
            for cell in cells:
                child = grid.clone()
                child.insertTile(cell, 4)
                children.append(child)
            self.childrenMin[key] = children

        minChild, minUtility = None, float('inf')

        for child in self.childrenMin[key]:
            _, _, utility = self.maximize(child, alpha, beta, depth + 1)

            if utility < minUtility:
                _, minChild, minUtility = _, child, utility

            if minUtility <= alpha:
                break

            if minUtility < beta:
                beta = minUtility

        return _, minChild, minUtility

    def evaluation(self, grid):
        key = h(grid)
        if key in self.heuristics:
            return self.heuristics[key]

        score = 0
        for i in range(4):
            for j in range(4):
                score += grid.map[i][j] * (6-i-j)
        #freeTiles = len(grid.getAvailableCells())
        #score -= score/(freeTiles+1)

        if not grid.canMove():
            lostPenalty = 2 * grid.getMaxTile()
            score -= lostPenalty

        self.heuristics[key] = score
        return score
        
    def timeOver(self):
        return self.startTime + timeLimit <= time.clock()