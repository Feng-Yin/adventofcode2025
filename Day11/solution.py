import re
import copy
import functools
import sys

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


def count_path(maze, start, end):
    if start not in maze:
        return 0

    @functools.lru_cache(maxsize=None)
    def _count_path(paths, end):
        if end in paths:
            return 1
        count = 0
        for stop in paths:
            if stop not in maze:
                return 0
            count += _count_path(tuple(maze[stop]), end)
        return count
    start_to_dac = _count_path(tuple(maze[start]), "dac")
    start_to_fft = _count_path(tuple(maze[start]), "fft")
    dac_to_fft = _count_path(tuple(maze["dac"]), "fft")
    fft_to_dac = _count_path(tuple(maze["fft"]), "dac")
    dac_to_end = _count_path(tuple(maze["dac"]), end)
    fft_to_end = _count_path(tuple(maze["fft"]), end)

    p1 = start_to_dac*dac_to_fft*fft_to_end
    p2 = start_to_fft*fft_to_dac*dac_to_end
    return p1+p2

def q2(maze, start, end):
    return count_path(maze, start, end)
       
with open("./input2.txt", "r") as file:
    maze = {}

    for line in file:
        line = line.strip()
        kv = line.split(':')
        key = kv[0].strip()
        value = kv[1].strip().split()
        #print(key, value)
        maze[key] = value

    #print("part 1: ", q1(maze, "you", "out"))
    print("part 2: ", q2(maze, "svr", "out"))