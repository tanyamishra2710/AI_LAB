import numpy as np
from PuzzleNode import *
import copy
import time
from queue import PriorityQueue
from itertools import count


def iterativeDeepeningSearch(startNode):
    maxLayer = 1
    while True:
        dfsList = []
        layer = 0
        dfsList.append((startNode, layer))

        while len(dfsList) != 0:
            top = dfsList.pop()
            tmpNode = top[0]
            tmpLayer = top[1]
            if tmpNode.isGoal():
                trace = []
                ptr = tmpNode
                while ptr is not None:
                    trace.append(ptr.node)
                    ptr = ptr.parent
                return tmpLayer, trace

            nextLayer = tmpLayer + 1
            if nextLayer > maxLayer:
                continue

            validMoves = tmpNode.getValidMoves()
            for moveChar in validMoves:
                nextNode = copy.deepcopy(tmpNode)
                nextNode.doMove(moveChar)
                if not inDFSNodeList(nextNode, dfsList):
                    dfsList.append((nextNode, nextLayer))
                    nextNode.parent = tmpNode
        maxLayer += 1


# check if tNode is in nList (used in iterativeDeepeningSearch())
# nList is a list of tuple (puzzleNode, layer)
def inDFSNodeList(tNode, nList):
    for node in nList:
        if (node[0].node == tNode.node).all():
            return True
    return False


# print solution trace
test = PuzzleNode()
test.shuffle()
test.show()
step, trace = iterativeDeepeningSearch(test)
print(step)
while len(trace) != 0:
    n = trace.pop()
    print(n)