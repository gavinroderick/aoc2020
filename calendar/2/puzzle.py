def parse(input):
    with open(input) as file:
        value_sets = []
        for line in file.readlines():
            value_sets.append(line.split())
        return value_sets
            
def solve(data):
    numberValid = 0
    for policy_set in data:
        if check_valid(int(policy_set[0].split("-")[0]), int(policy_set[0].split("-")[1]), policy_set[1].split(":")[0], policy_set[2] ):
            numberValid += 1
    return numberValid

def check_valid(minNumber, maxNumber, letter, password):
    return True if minNumber <= password.count(letter) <= maxNumber else False

print(solve(parse("input.txt")))