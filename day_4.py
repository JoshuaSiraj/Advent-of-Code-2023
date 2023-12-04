import re

f = open('./inputs/day_4.txt')

lines = f.readlines()
lines = [line.strip().split(':')[1].split('|') for line in lines]

def part_1(lines: list):

    total = 0

    for line in lines:
        winning_numbers = set([int(m.group()) for m in re.finditer('\d+', line[0])])
        test_numbers = set([int(m.group()) for m in re.finditer('\d+', line[1])])
        num_match = len(winning_numbers.intersection(test_numbers))
        if num_match > 0:
            total += 2**(num_match-1)
    
    return total


def part_2(lines: list):

    total = [1]*len(lines)

    for card_number, line in enumerate(lines):
        winning_numbers = set([int(m.group()) for m in re.finditer('\d+', line[0])])
        test_numbers = set([int(m.group()) for m in re.finditer('\d+', line[1])])
        num_match = len(winning_numbers.intersection(test_numbers))
        for n in range(num_match):
            total[card_number+n+1]+=1*total[card_number]


    return sum(total)

print(f'Part 1: {part_1(lines)}')
print(f'Part 2: {part_2(lines)}')