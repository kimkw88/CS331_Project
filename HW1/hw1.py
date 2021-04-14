# Author: Kwanghyuk Kim
# Due: April 19 2021
# CS 331
# Programming Assignment #1

import sys

# Breadth-First Search
def bfs(init, goal, outputFile):
    print("***** BFS mode:")
    writeFile = open(outputFile, "w")
    que_arr = []
    visited = []
    count_node = 0
    que_arr.append(init)
    visited.append(init)

    while True:
        state = que_arr.pop(0)
        count_node += 1
        print("Path", count_node, ":", state)
        print()
        writeFile.close()
        exit()


# Depth-First Search
def dfs(init, goal, outputFile):
    print("***** DFS mode:")

# Iterative-Deepening Depth First Search
def iddfs(init, goal, outputFile):
    print("***** ID-DFS mode:")

# A-star search
def astar(init, goal, outputFile):
    print("***** A* mode:")

def child_node(arr):
    boat = 1
    # Left boat
    if arr[0][2] == boat:
        # transport 1 chicken
        arr[0][0] = arr[0][0] - 1 # chicken
        arr[1][0] = arr[1][0] + 1 # chicken
        arr[0][2] = arr[0][2] - 1 # boat
        arr[1][2] = arr[1][2] + 1 # boat
        # transport 2 chickens
        arr[0][0] = arr[0][0] - 2 # chicken
        arr[1][0] = arr[1][0] + 2 # chicken
        arr[0][2] = arr[0][2] - 1 # boat
        arr[1][2] = arr[1][2] + 1 # boat
        # transport 1 wolf
        arr[0][1] = arr[0][1] - 1 # wolf
        arr[1][1] = arr[1][1] + 1 # wolf
        arr[0][2] = arr[0][2] - 1 # boat
        arr[1][2] = arr[1][2] + 1 # boat
        # transport 2 wolves
        arr[0][1] = arr[0][1] - 2 # wolf
        arr[1][1] = arr[1][1] + 2 # wolf
        arr[0][2] = arr[0][2] - 1 # boat
        arr[1][2] = arr[1][2] + 1 # boat
        # transport 1 chick and 1 wolf
        arr[0][0] = arr[0][0] - 1 # chicken
        arr[1][0] = arr[1][0] + 1 # chicken
        arr[0][1] = arr[0][1] - 1 # wolf
        arr[1][1] = arr[1][1] + 1 # wolf
        arr[0][2] = arr[0][2] - 1 # boat
        arr[1][2] = arr[1][2] + 1 # boat
    # Right boat
    elif arr[1][2] == boat:
        # transport 1 chicken
        arr[0][0] = arr[0][0] + 1 # chicken
        arr[1][0] = arr[1][0] - 1 # chicken
        arr[0][2] = arr[0][2] + 1 # boat
        arr[1][2] = arr[1][2] - 1 # boat
        # transport 2 chickens
        arr[0][0] = arr[0][0] + 2 # chicken
        arr[1][0] = arr[1][0] - 2 # chicken
        arr[0][2] = arr[0][2] + 1 # boat
        arr[1][2] = arr[1][2] - 1 # boat
        # transport 1 wolf
        arr[0][1] = arr[0][1] + 1 # wolf
        arr[1][1] = arr[1][1] - 1 # wolf
        arr[0][2] = arr[0][2] + 1 # boat
        arr[1][2] = arr[1][2] - 1 # boat
        # transport 2 wolves
        arr[0][1] = arr[0][1] + 2 # wolf
        arr[1][1] = arr[1][1] - 2 # wolf
        arr[0][2] = arr[0][2] + 1 # boat
        arr[1][2] = arr[1][2] - 1 # boat
        # transport 1 chick and 1 wolf
        arr[0][0] = arr[0][0] + 1 # chicken
        arr[1][0] = arr[1][0] - 1 # chicken
        arr[0][1] = arr[0][1] + 1 # wolf
        arr[1][1] = arr[1][1] - 1 # wolf
        arr[0][2] = arr[0][2] + 1 # boat
        arr[1][2] = arr[1][2] - 1 # boat

# check if chickens are greater than or equal to wolves
def check_GTE(arr):
    if arr[0][0] >= arr[0][1] and arr[1][0] >= arr[1][1]:
        return True
    else:
        if arr[0][0] == 0 or arr[1][0] == 0:
            return True
        else:
            return False


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
