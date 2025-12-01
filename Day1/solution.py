import re
import copy

def q1(maze, start, end):
    s = start
    e = end
    p = 0
    for l in maze:
        step = int(l[1:])
        if 'L' in l:
            s -= step
        else:
            s += step
        s %= 100
        if s == e:
            p += 1
    return p
    
def q2(maze, start, end):
    s = start
    e = end
    p = 0
    for l in maze:
        step = int(l[1:])
        p += int(step / 100)
        step %= 100
        bs = s
        if 'L' in l:
            s -= step
        else:
            s += step
        ns = s % 100
        if ns == e or ( s > 100 and bs != 0 ) or ( s < 0 and bs != 0):
            p += 1
        s = ns
    return p

with open("./input.txt", "r") as file:
    maze = []
    for line in file:
        line = line.strip()
        maze.append(line)
    print(q1(maze, 50, 0))
    print(q2(maze, 50, 0))
