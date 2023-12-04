import re

f = open('./inputs/day_3.txt')
lines = f.readlines()
lines = [line.strip() for line in lines]

def valid_indices(num_index:tuple, y_index, max_x, max_y):

    if num_index[0] - 1 >= 0:
        num_index = (num_index[0] - 1, num_index[1])
    
    if num_index[1] < max_x:
        num_index = (num_index[0], num_index[1] + 1)

    y_indices = [y_index]

    if y_index - 1 >= 0:
        y_indices.append(y_index - 1)
    
    if y_index + 1 < max_y:
        y_indices.append(y_index + 1)

    res = []

    for x in range(num_index[0], num_index[1]):
        for y in y_indices:
            res.append((x, y))

    return res

def part_1(lines):
    max_x = len(lines[0])
    max_y = len(lines)

    sum = 0

    for line_number, line in enumerate(lines):
        indices = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
        for idx in indices:
            check = False
            check_indices = valid_indices(idx, line_number, max_x, max_y)

            for val in check_indices:
                if not lines[val[1]][val[0]].isnumeric() and lines[val[1]][val[0]] != '.':
                    check = True
                    break
            
            if check:
                num = int(line[idx[0]:idx[1]])
                sum+=num
    
    return sum

def part_2(lines):
    max_x = len(lines[0])
    max_y = len(lines)

    sum = 0
    gears = {}

    for line_number, line in enumerate(lines):
        indices = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
        for idx in indices:
            check_indices = valid_indices(idx, line_number, max_x, max_y)

            for val in check_indices:
                if lines[val[1]][val[0]] == '*':
                    num = int(line[idx[0]:idx[1]])
                    if val in gears:
                        sum += gears[val]*num  
                    else:
                        gears[val] = num

                    break

    return sum

print(f'Part 1: {part_1(lines)}')
print(f'Part 2: {part_2(lines)}')