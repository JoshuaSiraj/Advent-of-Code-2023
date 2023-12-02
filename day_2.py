import re

f = open('./inputs/day_2.txt')
lines = f.readlines()
lines = [line.split(':')[1:][0] for line in lines]
lines = [line.split(';') for line in lines]

def part_1(lines):
    red_total = 12
    green_total = 13
    blue_total = 14
    sum = 0

    for game_idx, line in enumerate(lines):

        
        check = True
        for round in line:
            red = re.findall(r'\d+ red', round)
            if red != []:
                red = int(re.findall(r'\d+', red[0])[0])
            else:
                red = 0

            if red > red_total:
                check = False

            blue = re.findall(r'\d+ blue', round)
            if blue != []:
                blue = int(re.findall(r'\d+', blue[0])[0])
            else:
                blue = 0

            if blue > blue_total:
                check = False

            green = re.findall(r'\d+ green', round)
            if green != []:
                green = int(re.findall(r'\d+', green[0])[0])
            else:
                green = 0

            if green > green_total:
                check = False

        if check:
            sum += game_idx + 1
    
    return sum

def part_2(lines):
    sum = 0

    for line in lines:
        red_total = 0
        green_total = 0
        blue_total = 0
        
        for round in line:
            red = re.findall(r'\d+ red', round)
            if red != []:
                red = int(re.findall(r'\d+', red[0])[0])
            else:
                red = 0

            if red > red_total:
                red_total = red

            blue = re.findall(r'\d+ blue', round)
            if blue != []:
                blue = int(re.findall(r'\d+', blue[0])[0])
            else:
                blue = 0

            if blue > blue_total:
                blue_total = blue

            green = re.findall(r'\d+ green', round)
            if green != []:
                green = int(re.findall(r'\d+', green[0])[0])
            else:
                green = 0

            if green > green_total:
                green_total = green

        sum += red_total * blue_total * green_total

    return sum

print(f'Part 1: {part_1(lines)}')
print(f'Part 2: {part_2(lines)}')