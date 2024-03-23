# search.py͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃
# ---------͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃
# Licensing Information:  You are free to use or extend these projects for͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃 
# educational purposes provided that (1) you do not distribute or publish͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃 
# solutions, (2) you retain this notice, and (3) you provide clear͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃 
# attribution to UC Berkeley, including a link to͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃
# The core projects and autograders were primarily created by John DeNero͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃
# Student side autograding was added by Brad Miller, Nick Hay, and͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    visited = []
    frontier = util.Stack()
    frontier.push((problem.getStartState(), []))
    while not frontier.isEmpty():
        curr = frontier.pop()
        if problem.isGoalState(curr[0]):
            return curr[1]
        elif curr[0] in visited:
            continue
        visited.append(curr[0])
        for successor in problem.getSuccessors(curr[0]):
            frontier.push((successor[0], curr[1] + [successor[1]]))
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    visited = []
    frontier = util.Queue()
    frontier.push((problem.getStartState(), []))

    while not frontier.isEmpty():
        curr_state, curr_path = frontier.pop()

        if curr_state in visited:
            continue

        visited.append(curr_state)

        if problem.isGoalState(curr_state):
            return curr_path

        successors = problem.getSuccessors(curr_state)
        print(successors)  # Print successors outside the loop if you only want to see it once

        for successor in successors:
            next_state, action, _ = successor
            frontier.push((next_state, curr_path + [action]))

    util.raiseNotDefined()


def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    visited = []
    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), []), 0)
    while not frontier.isEmpty():
        curr = frontier.pop()
        if problem.isGoalState(curr[0]):
            return curr[1]
        elif curr[0] in visited:
            continue
        visited.append(curr[0])
        for successor in problem.getSuccessors(curr[0]):
            action = curr[1] + [successor[1]]
            frontier.push((successor[0], action), problem.getCostOfActions(action))
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    visited = []
    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), []), 0)
    while not frontier.isEmpty():
        curr = frontier.pop()
        if problem.isGoalState(curr[0]):
            return curr[1]
        elif curr[0] in visited:
            continue
        visited.append(curr[0])
        for successor in problem.getSuccessors(curr[0]):
            action = curr[1] + [successor[1]]
            heur = heuristic(successor[0], problem)
            frontier.push((successor[0], action), problem.getCostOfActions(action) + heur)
    util.raiseNotDefined()


# Abbreviations͏󠄂͏️͏󠄌͏󠄎͏󠄇͏󠄋͏󠄃
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
