import re
import copy

def q2_1(maze):
    path_db = []
    h = len(maze)
    w = len(maze[0])
    print(h, w)
    stack = []
    path = []
    path_cp = []
    maze_cp = copy.deepcopy(maze)
    for hi in range(h):
        for wi in range(w):
            if maze_cp[hi][wi] == '|':
                if hi + 1 < h: 
                    if maze_cp[hi+1][wi] == '^':
                        if wi - 1 >= 0:
                            maze_cp[hi+1][wi-1] = '|'
                            path_cp = copy.deepcopy(path)
                            path.append('L')
                        if wi + 1 < w:
                            path_cp.append('R')
                            stack.append(path_cp)
                    else:
                        maze_cp[hi+1][wi] = '|'
                        path.append('D')
    
    
    tmp = "".join(path)
    #print(tmp, len(path))
    path_db.append(tmp)
    count = 1
    wm = len(stack)
    while len(stack) > 0:
        wi = "".join(maze[0]).index('|')
        #print("init wi: ", wi)
        if len(stack) < wm:
            wm = len(stack)
            print("progress: ", wm, count)
        count += 1
        path = stack.pop()
        #print(path, len(path))
        e_path_len = len(path)
        path_cp = []
        #print("init path: ", path)
        for hi in range(h):
            if hi < e_path_len:
                if path[hi] == 'L':
                    wi -= 1
                elif path[hi] == 'R':
                    wi += 1
            else:
                if hi + 1 < h:
                    #print("check: ", hi+1, wi)
                    if maze[hi+1][wi] == '^':
                        path_cp = copy.deepcopy(path)
                        path.append('L')
                        wi -= 1
                        path_cp.append('R')
                        stack.append(path_cp)
                    else:
                        path.append('D')
        tmp = "".join(path)
        #print(tmp, len(path))
        if tmp not in path_db:
            path_db.append(tmp)
        else:
            print("xxxxxxxxxxxx")
            return 2
    
    return count
            


def q2(maze):
    path_db = []
    h = len(maze)
    w = len(maze[0])
    stack = []
    path = []
    path_cp = []
    maze_cp = copy.deepcopy(maze)
    for hi in range(h):
        for wi in range(w):
            if maze_cp[hi][wi] == '|':
                if hi + 1 < h: 
                    if maze_cp[hi+1][wi] == '^':
                        if wi - 1 >= 0:
                            maze_cp[hi+1][wi-1] = '|'
                            path_cp = copy.deepcopy(path)
                            path.append('L')
                        if wi + 1 < w:
                            path_cp.append('R')
                            stack.append(path_cp)
                    else:
                        maze_cp[hi+1][wi] = '|'
                        path.append('D')
    #for l in maze_cp:
    #    print(l)
    tmp = "".join(path)
    #print(tmp, len(path))
    path_db.append(tmp)
    #print("========")
    #print(stack)
    #print("========")
    count = 1
    wm = len(stack)
    while len(stack) > 0:
        if len(stack) < wm:
            wm = len(stack)
            print(wm, count)
        count += 1
        path = stack.pop()
        #print(path, len(path))
        e_path_len = len(path)
        maze_cp = copy.deepcopy(maze)
        path_cp = []
        for hi in range(h):
            for wi in range(w):
                if maze_cp[hi][wi] == '|':
                    if hi + 1 < h:
                        if maze_cp[hi+1][wi] == '^':
                            if hi < e_path_len:
                                if path[hi] == 'L':
                                    maze_cp[hi+1][wi-1] = '|'
                                elif path[hi] == 'R':
                                    maze_cp[hi+1][wi+1] = '|'      
                            else:
                                if wi - 1 >= 0:
                                    maze_cp[hi+1][wi-1] = '|'
                                    path_cp = copy.deepcopy(path)
                                    path.append('L')
                                if wi + 1 < w:
                                    path_cp.append('R')
                                    stack.append(path_cp)
                        else:
                            maze_cp[hi+1][wi] = '|'
                            if hi + 1 >= e_path_len:
                                path.append('D')
        #for l in maze_cp:
        #    print(l)
        tmp = "".join(path)
        #print(tmp, len(path))
        if tmp not in path_db:
            path_db.append(tmp)
        else:
            print("xxxxxxxxxxxx")
            return 2
        
    
    return count
    
    
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

with open("./input2.txt", "r") as file:
    maze = []
    for line in file:
        line = line.strip()
        if "S" in line:
            line = line.replace("S", "|")
        maze.append(list(line))
    print("part 1:", q1(copy.deepcopy(maze)))
    print("part 2:", q2_1(copy.deepcopy(maze)))
    #print("part 2.1:", q2(copy.deepcopy(maze)))
