import re
import copy

def q1(maze, symbol):
    w = len(maze[0])
    h = len(maze)
    result = 0
    for wi in range(w):
        tmp = 0
        if symbol[wi] == '*':
            tmp = 1
        for hi in range(h):
            if symbol[wi] == '*':
                tmp *= int(maze[hi][wi])
            elif symbol[wi] == '+':
                tmp += int(maze[hi][wi])
        result += tmp
    return result
    
def q2(maze, maze1, symbol):
    ranges = []
    w = len(maze[0])
    h = len(maze)
    result = 0
    for wi in range(w):
        mx = 0
        for hi in range(h):
            mx = max(mx, len(maze[hi][wi]))
        ranges.append(mx)
    pos = []
    start = 0
    for r in ranges:
        pos.append(range(start, start+r))
        start += r + 1
    for pi in range(len(pos)):
        st = pos[pi].start
        ed = pos[pi].stop
        tmp_r = 0
        if symbol[pi] == '*':
            tmp_r = 1
        for index in reversed(range(st, ed)):
            tmp_l = []
            for hi in range(h):
                if index < len(maze1[hi]) and maze1[hi][index] != ' ':
                    tmp_l.append(maze1[hi][index])
            #print(tmp_l)
            if len(tmp_l) == 0:
                continue
            num = int(''.join(tmp_l))
            if symbol[pi] == '+':
                tmp_r += num
            elif symbol[pi] == '*':
                tmp_r *= num
        result += tmp_r
    return result

with open("./input2.txt", "r") as file:
    maze = []
    symbol = []
    maze1 = []
    for line in file:
        if '+' in line or '*' in line:
            line = line.strip()
            line = line.split()
            symbol = line
        else:
            maze1.append(line[:-1])
            line = line.strip()
            line = line.split()
            #print(line)
            maze.append(line)
    print("part 1: ", q1(maze, symbol))
    print("part 2: ", q2(maze, maze1, symbol))
