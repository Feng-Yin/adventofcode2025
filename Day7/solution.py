import re
import copy
       
def q1(maze):
    h = len(maze)
    w = len(maze[0])
    for hi in range(h):
        for wi in range(w):
            if maze[hi][wi] == '|':
                #print(maze[hi])
                if hi + 1 < h: 
                    if maze[hi+1][wi] == '^':
                        if wi - 1 >= 0:
                            maze[hi+1][wi-1] = '|'
                        if wi + 1 < w:
                            maze[hi+1][wi+1] = '|'
                    else:
                        maze[hi+1][wi] = '|'
    #for l in maze:
    #    print(l)
    count = 0
    for hi in reversed(range(h)):
        for wi in range(w):
            if maze[hi][wi] == '^' and maze[hi-1][wi] == '|':
                count += 1
    return count

def q2(maze):
    h = len(maze)
    w = len(maze[0])
    maze_count = []
    for hi in range(h):
        tmp = []
        for wi in range(w):
            tmp.append(0)
        maze_count.append(tmp)
    maze_count[0][maze[0].index('|')] = 1
    for hi in range(h):
        for wi in range(w):
            if '|' in maze[hi][wi]:
                #print(maze[hi])
                if hi + 1 < h: 
                    if maze[hi+1][wi] == '^':
                        if wi - 1 >= 0:
                            if maze[hi+1][wi-1] == '.':
                                maze[hi+1][wi-1] = '|'
                                maze_count[hi+1][wi-1] = maze_count[hi][wi]
                            else:
                                maze[hi+1][wi-1] = '|'
                                maze_count[hi+1][wi-1] = maze_count[hi][wi]+maze_count[hi+1][wi-1]
                        if wi + 1 < w:
                            if maze[hi+1][wi+1] == '.':
                                maze[hi+1][wi+1] = '|'
                                maze_count[hi+1][wi+1] = maze_count[hi][wi]
                            else:
                                maze[hi+1][wi+1] = '|'
                                maze_count[hi+1][wi+1] = maze_count[hi][wi]+maze_count[hi+1][wi+1]
                    else:
                        if maze[hi+1][wi] == '.':
                            maze[hi+1][wi] = '|'
                            maze_count[hi+1][wi] = maze_count[hi][wi]
                        else:
                            maze[hi+1][wi] = '|'
                            maze_count[hi+1][wi] = maze_count[hi][wi]+maze_count[hi+1][wi]

    return sum(maze_count[-1])


with open("./input2.txt", "r") as file:
    maze = []
    for line in file:
        line = line.strip()
        if "S" in line:
            line = line.replace("S", "|")
        maze.append(list(line))
    print("part 1:", q1(copy.deepcopy(maze)))
    print("part 2:", q2(copy.deepcopy(maze)))
