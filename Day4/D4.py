import re
import copy

def roll_check(maze):
    cord = []
    result = 0
    max_y = len(maze)
    max_x = len(maze[0])
    #print("max_y ", max_y)
    #print("max_x ", max_x)
    for y in range(max_y):
        for x in range(max_x):
            #print("yx: ", y, x)
            #print("line: ", maze[y])
            if maze[y][x] != '@':
                continue
            buf = 0
            if y - 1 >= 0:
                if x - 1 >= 0 and maze[y-1][x-1] == '@':
                    buf += 1
                    if buf > 3:
                        continue
                if maze[y-1][x] == '@':
                    buf += 1
                    if buf > 3:
                        continue
                if x + 1 < max_x and maze[y-1][x+1] == '@':
                    buf += 1
                    if buf > 3:
                        continue
            if x - 1 >= 0 and maze[y][x-1] == '@':
                buf += 1
                if buf > 3:
                    continue
            if x + 1 < max_x and maze[y][x+1] == '@':
                buf += 1
                if buf > 3:
                    continue
            if y + 1 < max_y:
                if x - 1 >= 0 and maze[y+1][x-1] == '@':
                    buf += 1
                    if buf > 3:
                        continue
                if maze[y+1][x] == '@':
                    buf += 1
                    if buf > 3:
                        continue
                if x + 1 < max_x and maze[y+1][x+1] == '@':
                    buf += 1
                    if buf > 3:
                        continue
            #print(y, x)
            cord.append([y, x])
            result += 1

    for y, x in cord:
        maze[y][x] = '.'
    return result, maze


def q1(maze, start, end):
    maze_c = copy.deepcopy(maze)
    result, maze_new = roll_check(maze_c)
    return result
    
def q2(maze, start, end):
    r_final = 0
    maze_c = copy.deepcopy(maze)
    r_inter, maze_new = roll_check(maze_c)
    r_final += r_inter
    count = 0
    #print(count, r_inter)
    count += 1
    while r_inter > 0:
        maze_c = copy.deepcopy(maze_new)
        r_inter, maze_new = roll_check(maze_c)
        r_final += r_inter
        #print(count, r_inter)
        count += 1
    return r_final
    
    
with open("./input2.txt", "r") as file:
    maze = []
    for line in file:
        line = line.strip()
        maze.append(list(line))
        
    print("part 1: ", q1(maze, 0, 0))
    print("part 2: ", q2(maze, 0, 0))