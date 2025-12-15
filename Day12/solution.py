import re
import copy

def q1(maze, spaces):
    print(maze)
    print('*'*20)
    print(spaces)
    result = 0
    for sp in spaces:
        s = sp[0]
        r = 0
        for gi in range(len(sp[1:])):
            r += sp[gi+1]*maze[gi]
        if s >= r:
            result += 1
    return result
    
def q2(maze, spaces):
    pass

with open("./input2.txt", "r") as file:
    maze = [] # gifts size
    spaces = [] # space size + gifts
    gift_num = -1
    gift_size = 0
    for line in file:
        line = line.strip()
        if len(line) > 0 and line[-1] == ':':
            if gift_num != -1:
                maze.append(gift_size)
            gift_num = int(line[:-1])
            gift_size = 0
        elif '#' in line:
            gift_size += line.count('#')
        elif 'x' in line:
            if gift_num != -1:
                maze.append(gift_size)
                gift_num = -1
            ss = line.split(':')
            space_size = 1
            for s in ss[0].split('x'):
                space_size *= int(s)
            gifts = ss[1].strip().split()
            gifts = list(map(int, gifts))
            spaces.append([space_size] + gifts)
    print("part 1: ", q1(maze, spaces))
    print("part 2: ", q2(maze, spaces))

