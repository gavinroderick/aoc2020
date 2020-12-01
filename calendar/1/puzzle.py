def parse(input):
    with open(input) as file:
        data = [int(line.strip()) for line in file.readlines()]
        return data

def solve(data):
    for item in data:
        for next_item in data:
            if (2020 - item) - next_item == 0:
                return item * next_item

def solve_part_2(data):
    for item in data:
        for next_item in data:
            if (2020 - item) - next_item > 0:
                for anotha_one in data:
                    if ((2020 - item) - next_item) - anotha_one == 0:
                        return item * next_item * anotha_one
                        
print(solve(parse("input.txt")))
print(solve_part_2(parse("input.txt")))