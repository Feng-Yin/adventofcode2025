import re
import copy

def q1(maze, start, end):
    path_stack = []
    result = 0
    path_db = []
    for p in maze[start]:
        if p == end:
            result += 1
        else:
            path_stack.append([p])
    while len(path_stack) > 0:
        tmp_path = path_stack.pop()
        if tmp_path[-1] not in maze:
            #print("invalid next step: ", tmp_path[-1])
            continue
        next_stops = maze[tmp_path[-1]]
        for p in next_stops:
            if p == end:
                path_str = "".join(tmp_path) + end
                if path_str not in path_db:
                    result += 1
                    path_db.append(path_str)
                else:
                    print("foud dup path")
            else:
                if p not in tmp_path:
                    tmp_path_cp = copy.deepcopy(tmp_path)
                    tmp_path_cp.append(p)
                    path_stack.append(tmp_path_cp)
    return result

def debug(maze):
    ks = []
    for k, v in maze.items():
        if "out" in v:
            #print("remove: ", (k, v))
            ks.append(k)
    for k in ks:
        remove_invalid(maze, k, "out")
    
    print(maze)

def remove_invalid(maze, start, end):
    if start not in maze:
        return
    print("remove ", end, " from ", start, maze[start])
    maze[start] = list(set(maze[start]).symmetric_difference(set([end])))
    #print("after removal: ", maze[start])
    print("*"*30)
    if len(maze[start]) == 0:
        del maze[start]
        next_starts = []
        for k, v in maze.items():
            if start in v:
                next_starts.append(k)
        for ns in next_starts:
            remove_invalid(maze, ns, start)

def q2_debug(maze, start, end):
    path_stack = []
    path_db = []
    for p in maze[start]:
        if p == end:
            result += 1
        else:
            path_stack.append([p])
    loops = 0
    while len(path_stack) > 0:
        loops += 1
        if loops % 100000 == 0:
            print("stack depth: ", len(path_stack))
            print("path db: ", path_db)
        tmp_path = path_stack.pop()
        if tmp_path[-1] not in maze:
            if len(tmp_path) > 1:
                for i in reversed(range(len(path_stack))):
                    if tmp_path in path_stack[i]:
                        path_stack.pop(i)
            #print("remove ", tmp_path[-1], " from ", maze[tmp_path[-2]])
            #maze[tmp_path[-2]] = list(set(maze[tmp_path[-2]]).symmetric_difference(set([tmp_path[-1]])))
            #print("after removal: ", maze[tmp_path[-2]])
            continue
        next_stops = maze[tmp_path[-1]]
        for p in next_stops:
            if p == end:
                path_str = ",".join(tmp_path) + "," + end
                if path_str not in path_db:
                    path_db.append(path_str)
                else:
                    print("foud dup path")
            else:
                if p not in tmp_path:
                    tmp_path_cp = copy.deepcopy(tmp_path)
                    tmp_path_cp.append(p)
                    path_stack.append(tmp_path_cp)
                else:
                    print("found a loop :", ",".join(tmp_path) + "," + p)
        #loops -= 1
        #if loops == 0:
        #    break
    #print(path_db)
    print("*"*20)
    print(maze)    
    
    return len(path_db)

def cleanup_invalid_path(maze, tmp_path):
    for i in reversed(range(len(tmp_path))):
        if len(maze[tmp_path[i-1]]) == 1:
            continue
        else:
            for k in range(len(maze[tmp_path[i-1]])):
                if maze[tmp_path[i-1]][k] == tmp_path[i]:
                    print("remove ", tmp_path[i], " from ", tmp_path[i-1], maze[tmp_path[i-1]])
                    maze[tmp_path[i-1]].pop(k)
                    return
    
def q2(maze, start, end):
    path_stack = []
    path_db = []
    for p in maze[start]:
        path_stack.append([start, p])
    loops = 0
    while len(path_stack) > 0:
        loops += 1
        if loops % 100000 == 0:
            print("stack depth: ", len(path_stack))
            print("stack path len: ", len(path_stack[-1]))
            print("path db: ", len(path_db))
        tmp_path = path_stack.pop()
        next_stops = maze[tmp_path[-1]]
        for p in next_stops:
            if p == end:
                path_str = ",".join(tmp_path) + "," + end
                if path_str not in path_db:
                    if "dac" in path_str and "fft" in path_str:
                        path_db.append(path_str)
                    #else:
                        #print("invalid path: ", path_str)
                        #cleanup_invalid_path(maze, tmp_path)
                        #return 0
                else:
                    print("foud dup path: ", path_str)
            else:
                if p not in tmp_path:
                    tmp_path_cp = copy.deepcopy(tmp_path)
                    tmp_path_cp.append(p)
                    path_stack.append(tmp_path_cp)
                else:
                    print("found circle", ",".join(tmp_path)+","+p)
    #for p in path_db:
    #    if "dac" in p and "fft" in p:
    #        result += 1
    #for ps in path_stack:
    #    print(ps)
    return len(path_db)

with open("./input2.txt", "r") as file:
    maze = {}
    for line in file:
        line = line.strip()
        kv = line.split(':')
        key = kv[0].strip()
        value = kv[1].strip().split()
        #print(key, value)
        maze[key] = value
        
    print("part 1: ", q1(maze, "you", "out"))
    #print("part 1: ", q1(maze, "fft", "dac"))
    #print("svr -> fft", q2_debug(maze, "svr", "fft"))
    print("part 2: ", q2(maze, "svr", "out"))
    #debug(maze)
