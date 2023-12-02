import re

f = open('./inputs/day_1.txt')

lines = f.readlines()

lines = [line.rstrip() for line in lines]

def part_1(lines: list):

    sum = 0
    for line in lines:
        first = ''
        last = ''
        for char in line:
            if char.isnumeric():
                last = int(char)
                if first == '':
                    first = int(char)

        sum += first*10 + last

    return sum

def part_2(lines: list):

    eng_digits = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    ]

    sum = 0
    for line in lines:
        first = ''
        last = ''
        first_idx = 10e5
        last_idx = -1
        for idx, char in enumerate(line):
            if char.isnumeric():
                last = int(char)
                last_idx = idx
                if first == '':
                    first = int(char)
                    first_idx = idx

        
        for dig, english in enumerate(eng_digits):
            test_indices = [m.start() for m in re.finditer(english, line)]

            for test_idx in test_indices:
                if test_idx < first_idx:
                    first = dig +1
                    first_idx = test_idx

                if test_idx > last_idx:
                    last = dig+1
                    last_idx = test_idx
        
        sum += first*10 + last


    return sum

print(f'Part 1: {part_1(lines)}')
print(f'Part 2: {part_2(lines)}')