# Author: Kwanghyuk Kim
#         Hojun Shin
# Due: April 19 2021
# CS 331
# Programming Assignment #1

import sys
import copy

LEFT  = 0
RIGHT = 1
CHICKEN = 0
WOLVES  = 1
BOAT    = 2

class Node:
    def __init__(self, node, method, state):
        self.par_node = node

        # If boat is at left side
        if state[LEFT][BOAT] == 1:
            if method == 1:
                # transport 1 chicken
                state[LEFT][BOAT]        = 0
                state[LEFT][CHICKEN]    -= 1
                state[RIGHT][BOAT]       = 1
                state[RIGHT][CHICKEN]   += 1
            if method == 2:
                # transport 2 chickens
                state[LEFT][CHICKEN] -= 2 # chicken
                state[RIGHT][CHICKEN] += 2 # chicken
                state[LEFT][BOAT] = 0 # boat
                state[RIGHT][BOAT] = 1 # boat
            if method == 3:
                # transport 1 wolf
                state[LEFT][WOLVES] -= 1 # wolf
                state[RIGHT][WOLVES] += 1 # wolf
                state[LEFT][BOAT] = 0 # boat
                state[RIGHT][BOAT] = 1 # boat
            if method == 4:
                # transport 2 wolves
                state[LEFT][WOLVES] -= 2 # wolf
                state[RIGHT][WOLVES] += 2 # wolf
                state[LEFT][BOAT] = 0 # boat
                state[RIGHT][BOAT] = 1 # boat
            if method == 5:
                # transport 1 chick and 1 wolf
                state[LEFT][CHICKEN] -= 1 # chicken
                state[RIGHT][CHICKEN] += 1 # chicken
                state[LEFT][WOLVES] -= 1 # wolf
                state[RIGHT][WOLVES] += 1 # wolf
                state[LEFT][BOAT] = 0 # boat
                state[RIGHT][BOAT] = 1 # boat
        elif state[RIGHT][BOAT] == 1:
            if method == 1:
                # transport 1 chicken
                state[LEFT][CHICKEN] += 1 # chicken
                state[RIGHT][CHICKEN] -= 1 # chicken
                state[LEFT][BOAT] = 1 # boat
                state[RIGHT][BOAT] = 0 # boat
            if method == 2:
                # transport 2 chickens
                state[LEFT][CHICKEN] += 2 # chicken
                state[RIGHT][CHICKEN] -= 2 # chicken
                state[LEFT][BOAT] = 1 # boat
                state[RIGHT][BOAT] = 0 # boat
            if method == 3:
                # transport 1 wolf
                state[LEFT][WOLVES] += 1 # wolf
                state[RIGHT][WOLVES] -= 1 # wolf
                state[LEFT][BOAT] = 1 # boat
                state[RIGHT][BOAT] = 0 # boat
            if method == 4:
                # transport 2 wolves
                state[LEFT][WOLVES] += 2 # wolf
                state[RIGHT][WOLVES] -= 2 # wolf
                state[LEFT][BOAT] = 1 # boat
                state[RIGHT][BOAT] = 0 # boat
            if method == 5:
                # transport 1 chick and 1 wolf
                state[LEFT][CHICKEN] += 1 # chicken
                state[RIGHT][CHICKEN] -= 1 # chicken
                state[LEFT][WOLVES] += 1 # wolf
                state[RIGHT][WOLVES] -= 1 # wolf
                state[LEFT][BOAT] = 1 # boat
                state[RIGHT][BOAT] = 0 # boat
            
        # check if chickens are greater than or equal to wolves
        if state[LEFT][CHICKEN] < 0 or state[LEFT][CHICKEN] > 3:
            method = 0
        if state[LEFT][WOLVES] < 0 or state[LEFT][WOLVES] > 3:
           method = 0
        if state[RIGHT][CHICKEN] < 0 or state[RIGHT][CHICKEN] > 3:
            method = 0
        if state[RIGHT][WOLVES] < 0 or state[RIGHT][WOLVES] > 3:
            method = 0
        if state[LEFT][CHICKEN] != 0 and state[LEFT][CHICKEN] < state[LEFT][WOLVES]:
            method = 0
        if state[RIGHT][CHICKEN] != 0 and state[RIGHT][CHICKEN] < state[RIGHT][WOLVES]:
            method = 0

        self.state = state
        self.method = method


# Breadth-First Search
def bfs(init, goal, outputFile):
    print("***** BFS mode:")
    que_list  = []
    visited  = []
    solution = []
    node_list = []
    count = 0

    # Initial state node
    init_node = Node(-1, 0, init)
    node_list.append(init_node)
    que_list.append(init_node)

    while True:
        cur_node = que_list.pop(0)
        count += 1
        
        if not (cur_node.state in visited):
            if cur_node.state == goal:
                break
            else:
                visited.append(cur_node.state)

                # Create, append, que child node
                for i in range(1, 6):
                    child_node = Node(node_list.index(cur_node), i, copy.deepcopy(cur_node.state))
                    if child_node.method != 0:
                        node_list.append(child_node)
                        que_list.append(child_node)

    solution_count = 0

    while True:
        solution.append(cur_node)
        solution_count += 1
        if cur_node.par_node == -1:
            break
        cur_node = node_list[cur_node.par_node]

    solution.reverse()
    print("Reached Goal!")
    print("Solution: ")
    for x in solution:
        print(x.state)
    print("Solution count: ", solution_count)
    print("Expanded count: ", count)

# Depth-First Search
def dfs(init, goal, outputFile):
    print("***** DFS mode:")
    stack_list  = []
    visited  = []
    solution = []
    node_list = []
    count = 0

    # Initial state node
    init_node = Node(-1, 0, init)
    node_list.append(init_node)
    stack_list.append(init_node)

    while True:
        cur_node = stack_list.pop()
        count += 1
        
        if not (cur_node.state in visited):
            if cur_node.state == goal:
                break
            else:
                visited.append(cur_node.state)

                # Create, append, que child node
                for i in range(1, 6):
                    child_node = Node(node_list.index(cur_node), i, copy.deepcopy(cur_node.state))
                    if child_node.method != 0:
                        node_list.append(child_node)
                        stack_list.append(child_node)

    solution_count = 0

    while True:
        solution.append(cur_node)
        solution_count += 1
        if cur_node.par_node == -1:
            break
        cur_node = node_list[cur_node.par_node]

    solution.reverse()
    print("Reached Goal!")
    print("Solution: ")
    for x in solution:
        print(x.state)
    print("Solution count: ", solution_count)
    print("Expanded count: ", count)

# Iterative-Deepening Depth First Search
def iddfs(init, goal, outputFile):
    print("***** ID-DFS mode:")
    

# A-star search
def astar(init, goal, outputFile):
    print("***** A* mode:")


def readfile(filename):
    file = open(filename, "r")
    state = []
    for i in range(0,2):
        line = file.readline().strip()
        val = []
        for j in line.split(','):
            val.append(int(j))
        state.append(val)
    file.close()
    return state

def main():
    if len(sys.argv) != 5:
        print("Invalid Input! Please take the following command line 5 arguments:\n\thw1.py <initial state file> <goal state file> <mode> <output file>\n")
        exit()
    else:
        init = readfile(sys.argv[1])
        print("init:", init)
        goal = readfile(sys.argv[2])
        print("goal:", goal)
        mode = sys.argv[3]
        output = sys.argv[4]

        if mode == 'bfs':
            bfs(init, goal, output)
        elif mode == 'dfs':
            dfs(init, goal, output)
        elif mode == 'iddfs':
            iddfs(init, goal, output)
        elif mode == 'astar':
            astar(init, goal, output)
        else:
            print("Invalid mode. Please try again.")
            exit()

    
if __name__ == "__main__":
    main()