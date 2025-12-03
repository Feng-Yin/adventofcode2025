import re
import copy

    
def q1(maze, start, end):
    result = 0
    for line in maze:
        max_value1 = max(line)
        index = line.index(max_value1)
        if index == len(line) - 1:
            max_value2 = max(line[:index])
            result += max_value2 *10 + max_value1
        else:
            max_value2 = max(line[index + 1:])
            result += max_value1 *10 + max_value2
    return result

def q2(maze, start, end):
    result = 0
    for line in maze:
        res_list = []
        start_index = 0
        for i in range(12):
            max_value = max(line[start_index:len(line) - 12 + i + 1])
            start_index = line.index(max_value, start_index, len(line) - 12 + i + 1) + 1
            res_list.append(max_value)

        string_list = map(str, res_list)
        result_string = "".join(string_list)
        #print(result_string)

        result += int(result_string)
    return result

with open("./input.txt", "r") as file:
    maze = []
    for line in file:
        line = line.strip()
        maze.append([int(x) for x in list(line)])
    
    print("Part 1:", q1(maze, 0, 0))
    print("Part 2:", q2(maze, 0, 0))

