import re
import copy
import itertools

def q1(ranges, ids):
    result = 0
    for i in ids:
        for r in ranges:
            if i in r:
                #print(i, r)
                result += 1
                break
    return result

def add_nr(i, ranges):
    r = ranges[i]
    ret = []
    for nr in ranges[i+1:]:
        o_r = range(max(r.start, nr.start), min(r.stop, nr.stop))
        if len(o_r) > 0:
            if r.start != o_r.start:
                ret.append(range(r.start, o_r.start))
            if r.stop != o_r.stop:
                ret.append(range(o_r.stop, r.stop))
            #print("check: ", r, nr)
            #print("breaks: ", ret)
            return ret
    return [r]

def q2(ranges, ids):
    new_ranges = []
    while True:
        for i in range(len(ranges)):
            b_rs = add_nr(i, ranges)
            if len(b_rs) != 0:
                new_ranges.extend(b_rs)
            #print("ranges: ", ranges)
            #print("new_ranges: ", new_ranges)
            #print("================")
        if ranges == new_ranges:
            break
        ranges = new_ranges
        new_ranges = []
        
    #print(new_ranges)
    total_len = 0
    for r in new_ranges:
        total_len += len(r)
    return total_len

with open("./input2.txt", "r") as file:
    ranges = []
    ids = []
    for line in file:
        line = line.strip()
        if line == "":
            continue
        if '-' in line:
            rs = line.split('-')
            ranges.append(range(int(rs[0]), int(rs[1]) + 1))
            if int(rs[1]) + 1 <= int(rs[0]):
                print("xxxxxxxxxxxxxxx")
        else:
            ids.append(int(line))
    print("part 1: ", q1(ranges, ids))
    print("part 2: ", q2(ranges, ids))
