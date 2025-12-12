import re
import copy
from itertools import combinations

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
    
def is_done(joltage):
    ret = 0
    for n in joltage:
        if n != 0:
            ret += 1
    return ret

def get_buttons(buttons, step):
    valid_buttons = []
    for button in buttons:
        if len(button) == step:
            valid_buttons.append(button)
    return valid_buttons

def joltage_sum(button, joltage):
    result = 0
    for b in button:
        result += joltage[b]
    return result

def push(buttons, step, joltage):
    valid_buttons = get_buttons(buttons, step)
    max_push = 0
    push_map = {}
    for button in valid_buttons:
        min_joltage = max(joltage)
        for b in button:
            min_joltage = min(min_joltage, joltage[b])
        if min_joltage in push_map:
            push_map[min_joltage].append(button)
        else:
            push_map[min_joltage] = [button]
        max_push = max(max_push, min_joltage)
    
    if max_push > 0:
        i = 0
        b_sum = 0
        for bi in range(len(push_map[max_push])):
            print("check: ", push_map[max_push], bi)
            j_sum = joltage_sum(push_map[max_push][bi], joltage)
            if b_sum < j_sum:
                b_sum = j_sum
                i = bi

        print("push: ", max_push, push_map[max_push][i])
        for b in push_map[max_push][i]:
            joltage[b] = joltage[b] - max_push
    
    return max_push, joltage
        

def q2(maze):
    result = 0
    for r in maze:
        buttons = r[1]
        joltage = r[2]
        max_b_len = 0
        for b in buttons:
            max_b_len = max(max_b_len, len(b))
        joltage_copy = copy.deepcopy(joltage)
        
        non_zero = is_done(joltage_copy)
        step = min(non_zero, max_b_len)
        while non_zero > 0:
            print("do: ", r[2], joltage_copy)
            max_push, joltage_copy = push(buttons, step, joltage_copy)
            result += max_push
            if is_done(joltage_copy) == 0:
                print("done: ", r)
                break
            if max_push == 0:
                step -= 1
                if step <= 0:
                    return 0
            else:
                step = min(step, is_done(joltage_copy))
    return result

with open("./input.txt", "r") as file:
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
    print("part 2: ", q2(maze))
