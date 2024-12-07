from tqdm import tqdm
from itertools import product

def read_input(path):
    input_dict = {}
    with open(path) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        lst = line.split(":")
        key = int(lst[0])
        lst2 = lst[1].strip().split(" ")
        numbs = [int(j) for j in lst2]
        input_dict[key] = numbs
    return input_dict

def calculate_combination(list, combination):
    result = list[0]
    for i,op in enumerate(combination):
        if op == 0:
            result += list[i+1]
        elif op == 1:
            result *= list[i+1]
        elif op == 2:
            result = int(str(result)+(str(list[i+1])))
    return result

def hash_combination(combination):
    hash = combination[0]
    for c in combination[1:]:
        hash = hash*10 + c
    return hash

def unhash_combination(hash, n):
    list = [0 for _ in range(n)]
    hash = str(hash)
    if n<len(hash):
        raise ValueError("This hash cannot be from a combination this long")
    for i, h in enumerate(hash[::-1]):
            list[-(i+1)] = int(h)
    return list

def check_line(key, numbers, version = 1):
    pos_comb = possible_combinations(len(numbers)-1, version) # all possible combination hashes
    for c in pos_comb:
        combination = unhash_combination(c, len(numbers)-1)
        res = calculate_combination(numbers, combination)
        if res == key:
            return True
    return False

def possible_combinations(n, x):
    result = set()
    for length in range(1, n + 1):  # Iterate through all possible lengths
        for digits in product(range(x + 1), repeat=length):
            number = int("".join(map(str, digits)))  # Create a number from the digits
            result.add(number)
    return result

def part_one(dict):
    ans = 0

    for key in tqdm(dict.keys()):
        numb = dict[key]
        res = check_line(key, numb)
        if res:
            ans += key
    return ans

def part_two(dict):
    ans = 0
    for key in tqdm(dict.keys()):
        numb = dict[key]
        res = check_line(key, numb, version=2)
        if res:
            ans += key
    return ans

PATH = r'Day_7\input.txt'
DICT = read_input(PATH)

ans1 = part_one(DICT)
ans2 = part_two(DICT)











    








