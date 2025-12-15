import re
import copy
from itertools import combinations
import z3

def get_diff(buttons):
    diff = []
    for button in buttons:
        diff = list(set(diff).symmetric_difference(set(button)))
    return diff

def can_work(lights, buttons, num_buttons):
    for bs in combinations(buttons, num_buttons):
        ls = get_diff(bs)
        ls.sort()
        if ls == lights:
            return True
    return False

def q1(maze):
    result = 0
    #print(maze)
    for r in maze:
        lights = r[0]
        buttons = r[1]
        for num_buttons in range(1, len(buttons)):
            if can_work(lights, buttons, num_buttons):
                result += num_buttons
                break
    return result

def q2_z3(maze):
    result = 0
    for r in maze:
        s = z3.Optimize()
        # var for each button
        vars = [z3.Int(f'button_{i}') for i in range(len(r[1]))]
        # press >= 0
        for v in vars:
            s.add(v>=0)
        for li in range(len(r[2])):
            sum_level = sum(vars[bi] for bi in range(len(r[1])) if li in r[1][bi])
            s.add(sum_level == r[2][li])
        s.minimize(z3.Sum(vars))
        if s.check() == z3.sat:
            m = s.model()
            result += sum(m[i].as_long() for i in m)

    return result

with open("./input2.txt", "r") as file:
    maze = []
    for line in file:
        line = line.strip()
        index1 = line.find('[')
        index2 = line.find(']')
        index3 = line.find('{')
        index4 = line.find('}')
        lights = line[index1+1:index2]
        lights = list(lights)
        tmp = []
        for i in range(len(lights)):
            if lights[i] == '#':
                tmp.append(i)
        lights = tmp
        buttons = line[index2+3:index3-2]
        buttons = buttons.split(") (")
        for i in range(len(buttons)):
            buttons[i] = buttons[i].split(',')
            buttons[i] = list(map(int, buttons[i]))
        joltage = line[index3+1:index4]
        joltage = joltage.split(',')
        joltage = list(map(int, joltage))
        maze.append([lights, buttons, joltage])
    
    #s1 = [1,2,3,5]
    #s2 = [5,6,7,8]
    #s = set(s1).symmetric_difference(set(s2))
    #print(list(s))
    print("part 1: ", q1(maze))
    print("part 2: ", q2_z3(maze))
