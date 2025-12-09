import re
import copy

def q1(maze):
    areas = {}
    max_area = 0
    #print(maze)
    for i in range(len(maze)-1):
        for j in range(i+1, len(maze)):
            area = abs(int(maze[i][0])-int(maze[j][0])+1) * abs(int(maze[i][1])-int(maze[j][1])+1)
            key = maze[i][0]+','+maze[i][1]+','+maze[j][0]+','+maze[j][1]
            areas[key] = area
            max_area = max(max_area, area)
    
    return max_area

def is_accepted(keys, xy, yx):
    for key in keys:
        ret = True
        ps = key.split(',')
        p1_x = int(ps[0])
        p1_y = int(ps[1])
        p2_x = int(ps[2])
        p2_y = int(ps[3])
        #print("check: ", [p1_x, p1_y], [p2_x, p2_y])
        for yi in range(min(p1_y, p2_y), max(p1_y, p2_y)+1):
            min_x = min(p1_x, p2_x)
            max_x = max(p1_x, p2_x)
            if min_x < yx[yi][0] or max_x > yx[yi][1]:
                ret = False
                break
    return ret
    
def q2(maze):
    areas = {}
    max_area = 0
    max_x = 0
    max_y = 0
    #print(maze)
    for i in range(len(maze)-1):
        for j in range(i+1, len(maze)):
            area = (abs(int(maze[i][0])-int(maze[j][0]))+1) * (abs(int(maze[i][1])-int(maze[j][1]))+1)
            max_x = max(max_x, int(maze[i][0]))
            max_x = max(max_x, int(maze[j][0]))
            max_y = max(max_y, int(maze[i][1]))
            max_y = max(max_y, int(maze[j][1]))
            
            key = maze[i][0]+','+maze[i][1]+','+maze[j][0]+','+maze[j][1]
            if area in areas:
                areas[area].append(key)
            else:
                areas[area] = [key]
            max_area = max(max_area, area)
    xy = {}
    yx = {}
    print("create initial xy and yx")
    for i in range(len(maze)):
        x = int(maze[i][0])
        y = int(maze[i][1])
        if x in xy:
            xy[x].append(y)
        else:
            xy[x] = [y]
        if y in yx:
            yx[y].append(x)
        else:
            yx[y] = [x]
    print("created initial xy and yx")
    xy_copy = copy.deepcopy(xy)
    print("re-init yx")
    for yk in yx.keys():
        xs = yx[yk]
        xs.sort()
        for xi in range(xs[0]+1, xs[-1]):
            if xi in xy:
                xy[xi].append(yk)
                xy[xi].sort()
                xy[xi] = [xy[xi][0], xy[xi][-1]]
            else:
                xy[xi] = [yk]
    print("re-init xy")
    for xk in xy_copy.keys():
        ys = xy_copy[xk]
        ys.sort()
        for yi in range(ys[0]+1, ys[-1]):
            if yi in yx:
                yx[yi].append(xk)
                yx[yi].sort()
                yx[yi] = [yx[yi][0], yx[yi][-1]]
            else:
                yx[yi] = [xk]
    print("sort areas")
    sorted_areas = list(areas.keys())
    sorted_areas.sort(reverse=True)
    print("sorted areas")
    #print(areas)
    for area in sorted_areas:
        #print("check area: ", area)
        if is_accepted(areas[area], xy, yx):
            return area
    return 0

with open("./input2.txt", "r") as file:
    maze = []
    for line in file:
        line = line.strip()
        maze.append(line.split(','))
    print("part 1: ", q1(maze))
    print("part 2: ", q2(maze))
