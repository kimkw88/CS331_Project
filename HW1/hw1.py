# Author: Kwanghyuk Kim
#         Hojun Shin
# Due: April 19 2021
# CS 331
# Programming Assignment #1

import sys
import copy
import Queue

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
            if method == 5:
                # transport 2 wolves
                state[LEFT][WOLVES] -= 2 # wolf
                state[RIGHT][WOLVES] += 2 # wolf
                state[LEFT][BOAT] = 0 # boat
                state[RIGHT][BOAT] = 1 # boat
            if method == 4:
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
            if method == 5:
                # transport 2 wolves
                state[LEFT][WOLVES] += 2 # wolf
                state[RIGHT][WOLVES] -= 2 # wolf
                state[LEFT][BOAT] = 1 # boat
                state[RIGHT][BOAT] = 0 # boat
            if method == 4:
                # transport 1 chick and 1 wolf
                state[LEFT][CHICKEN] += 1 # chicken
                state[RIGHT][CHICKEN] -= 1 # chicken
                state[LEFT][WOLVES] += 1 # wolf
                state[RIGHT][WOLVES] -= 1 # wolf
                state[LEFT][BOAT] = 1 # boat
                state[RIGHT][BOAT] = 0 # boat
            
        # check if chickens are greater than or equal to wolves
        if not (state[LEFT][CHICKEN] >= 0 \
           and state[LEFT][WOLVES] >= 0 \
           and state[RIGHT][CHICKEN] >= 0 \
           and state[RIGHT][WOLVES] >= 0 \
           and (state[LEFT][CHICKEN] == 0 or state[LEFT][CHICKEN] >= state[LEFT][WOLVES]) \
           and (state[RIGHT][CHICKEN] == 0 or state[RIGHT][CHICKEN] >= state[RIGHT][WOLVES])):
            method = 0

        self.state = state
        self.method = method


def traceback(node, count, output):
    solution = []
    solution_arr = []
    solution_count = 0
    while node != None:
        if node.method == 1:
            solution.append("Put one chicken in the boat")
        elif node.method == 2:
            solution.append("Put two chickens in the boat")
        elif node.method == 3:
            solution.append("Put one wolf in the boat")
        elif node.method == 4:
            solution.append("Put one wolf and one chicken in the boat")
        elif node.method == 5:
            solution.append("Put two wolves in the boat")
        solution_arr.append(node.state)
        solution_count += 1
        node = node.par_node

    solution.reverse()
    solution_arr.reverse()
    file = open(output, "w")
    for x in solution:
        print(x)
        file.write(x + "\n")
    #for y in solution_arr:
        #print(y)
    print("Solution count: " + str(solution_count))
    file.write("Solution count: " + str(solution_count) + "\n")
    print("Expanded count: " + str(solution_count))
    file.write("Expanded count: " + str(count) + "\n")
    file.close()

# Breadth-First Search
def bfs(init, goal):
    print("***** BFS mode:")
    # Initial state node
    que  = Queue.Queue()
    que.put(Node(None, 0, init))
    explored  = set()
    expanded = 0

    while que:
        cur_node = que.get()
        explored.add(tuple(tuple(i) for i in cur_node.state))

        # Create, append, que child node
        for i in range(1, 6):
            child_node = Node(cur_node, i, copy.deepcopy(cur_node.state))
            if child_node.method != 0:
                expanded += 1
                if tuple(tuple(i) for i in child_node.state) not in explored:
                    if child_node.state == goal:
                        return child_node, expanded
                    que.put(child_node)


# Depth-First Search
def dfs(init, goal):
    print("***** DFS mode:")
    # Initial state node
    que = Queue.LifoQueue()
    que.put(Node(None, 0, init))
    explored  = set()
    expanded = 0

    while que:
        cur_node = que.get()
        explored.add(tuple(tuple(i) for i in cur_node.state))

        # Create, append, que child node
        for i in range(1, 6):
            child_node = Node(cur_node, i, copy.deepcopy(cur_node.state))
            if child_node.method != 0:
                expanded += 1
                if tuple(tuple(i) for i in child_node.state) not in explored:
                    if child_node.state == goal:
                        return child_node, expanded
                    que.put(child_node)


# Depth-Limited Search
def dls(init, goal, limit, expanded):
    initial_node = Node(None, None, init)
    return dls_(initial_node, goal, limit, expanded)

def dls_(node, goal, limit, expanded):
    if node.state == goal:
        return node, expanded
    elif limit == 0:
        return "stop"
    else:
        stop = False
        for i in range(1, 6):
            child_node = Node(node, i, copy.deepcopy(node.state))
            if child_node.method != 0:
                expanded += 1
                res = dls_(child_node, goal, limit - 1, expanded)
                if res == "stop":
                    stop = True
                elif res:
                    return res
        if stop:
            return "stop"
        else:
            return False

# Iterative-Deepening Depth First Search
def iddfs(init, goal):
    print("***** ID-DFS mode:")
    expanded = 0
    max_depth = 10000000
    for limit in range(max_depth):
        res = dls(init, goal, limit, expanded)
        if res != "stop":
            return res


def eval(state, goal):
    return (goal[LEFT][CHICKEN] + goal[LEFT][WOLVES] - state[LEFT][CHICKEN] - state[LEFT][WOLVES])

# A-star search
def astar(init, goal):
    print("***** A* mode:")
    initial_node = Node(None, None, init)
    que = Queue.PriorityQueue()
    que.put((eval(initial_node.state, goal), initial_node))
    explored = set()
    expanded = 0

    while que:
        cur_node = que.get()[1]
        explored.add(tuple(tuple(i) for i in cur_node.state))

        # Create, append, que child node
        for i in range(1, 6):
            child_node = Node(cur_node, i, copy.deepcopy(cur_node.state))
            if child_node.method != 0:
                expanded += 1
                if tuple(tuple(i) for i in child_node.state) not in explored:
                    if child_node.state == goal:
                        return child_node, expanded
                    que.put((eval(child_node.state, goal), child_node))



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
        print("init:" + str(init))
        goal = readfile(sys.argv[2])
        print("goal:" + str(goal))
        mode = sys.argv[3]
        output = sys.argv[4]

        if mode == 'bfs':
            res = bfs(init, goal)
        elif mode == 'dfs':
            res = dfs(init, goal)
        elif mode == 'iddfs':
            res = iddfs(init, goal)
        elif mode == 'astar':
            res = astar(init, goal)
        else:
            print("Invalid mode. Please try again.")
            exit()

    traceback(res[0], res[1], output)

    
if __name__ == "__main__":
    main()