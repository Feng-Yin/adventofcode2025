import re
import copy


def q1(maze, start, end):
    res = 0
    for row in maze:
        ss = re.split('-', row)
        s = int(ss[0])
        e = int(ss[1])
        for i in range(s, e + 1):
            i_str = str(i)
            if len(i_str) % 2 == 0 and i_str[0:int(len(i_str)/2)] == i_str[int(len(i_str)/2):]:
                res += i
    return res
    
def q2(maze, start, end):
    res = 0
    for row in maze:
        ss = re.split('-', row)
        s = int(ss[0])
        e = int(ss[1])
        for i in range(s, e + 1):
            for i_len in range(1, len(str(i))):
                if len(str(i)) % i_len == 0:
                    seg = int(len(str(i)) / i_len)
                    if str(i)[0:i_len] * seg == str(i):
                        res += i
                        break
    return res

with open("./input.txt", "r") as file:
    maze = []
    for line in file:
        line = line.strip()
        maze.append(re.split(',', line))

    print("Part 1:", q1(maze[0], 0, 0))
    print("Part 2:", q2(maze[0], 0, 0))

