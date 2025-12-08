import re
import copy
import math

def in_c_group(c_group, p):
    for i in range(len(c_group)):
        if p in c_group[i]:
            return i
    return -1

def q1(maze):
    dis_map = {}
    for i in range(len(maze)-1):
        for j in range(i+1, len(maze)):
            dis = math.dist([int(maze[i][0]), int(maze[i][1]), int(maze[i][2])], [int(maze[j][0]), int(maze[j][1]), int(maze[j][2])])
            if dis not in dis_map:
                dis_map[dis] = [[maze[i], maze[j]]]
            else:
                dis_map[dis].append([maze[i], maze[j]])
                print("same distance")
    #print(dis_map)
    keys = list(dis_map.keys())
    print(len(keys))
    keys.sort()
    #print(keys)
    c_group = []
    #for i in range(len(keys)):
    for i in range(1000):
        #print("Handle: ", i, dis_map[keys[i]])
        for pairs in dis_map[keys[i]]:
            p0 = pairs[0][0]+','+pairs[0][1]+','+pairs[0][2]
            p1 = pairs[1][0]+','+pairs[1][1]+','+pairs[1][2]
            #print("handle: ", p0, p1)
            p0_i = in_c_group(c_group, p0)
            p1_i = in_c_group(c_group, p1)
            if p0_i == -1 and p1_i == -1:
                c_group.append([p0, p1])
                #print("new pair: ", p0, p1)
            elif p0_i != -1 and p1_i == -1:
                c_group[p0_i].append(p1)
            elif p0_i == -1 and p1_i != -1:
                c_group[p1_i].append(p0)
            elif p0_i != -1 and p1_i != -1 and p0_i != p1_i:
                c_group[p0_i].extend(c_group[p1_i])
                c_group.pop(p1_i)
                
            #print("c_group: ", c_group)
    c_group.sort(key=len, reverse=True)
    #print(c_group)
    result = 1
    for i in range(3):
        result *= len(c_group[i])
    return result
                
    
def q2(maze):
    dis_map = {}
    for i in range(len(maze)-1):
        for j in range(i+1, len(maze)):
            dis = math.dist([int(maze[i][0]), int(maze[i][1]), int(maze[i][2])], [int(maze[j][0]), int(maze[j][1]), int(maze[j][2])])
            if dis not in dis_map:
                dis_map[dis] = [[maze[i], maze[j]]]
            else:
                dis_map[dis].append([maze[i], maze[j]])
                print("same distance")
    #print(dis_map)
    keys = list(dis_map.keys())
    print(len(keys))
    keys.sort()
    #print(keys)
    c_group = []
    for i in range(len(keys)):
    #for i in range(10):
        #print("Handle: ", i, dis_map[keys[i]])
        for pairs in dis_map[keys[i]]:
            p0 = pairs[0][0]+','+pairs[0][1]+','+pairs[0][2]
            p1 = pairs[1][0]+','+pairs[1][1]+','+pairs[1][2]
            #print("handle: ", p0, p1)
            p0_i = in_c_group(c_group, p0)
            p1_i = in_c_group(c_group, p1)
            if p0_i == -1 and p1_i == -1:
                c_group.append([p0, p1])
                #print("new pair: ", p0, p1)
            elif p0_i != -1 and p1_i == -1:
                c_group[p0_i].append(p1)
            elif p0_i == -1 and p1_i != -1:
                c_group[p1_i].append(p0)
            elif p0_i != -1 and p1_i != -1 and p0_i != p1_i:
                c_group[p0_i].extend(c_group[p1_i])
                c_group.pop(p1_i)
            if len(c_group) == 1 and len(c_group[0]) == len(maze):
                #print(c_group)
                return int(pairs[0][0])*int(pairs[1][0])

    return 0

with open("./input2.txt", "r") as file:
    maze = []
    for line in file:
        line = line.strip()
        cord = line.split(',')
        maze.append(cord)
    print("part 1: ", q1(maze))
    print('part 2: ', q2(maze))

