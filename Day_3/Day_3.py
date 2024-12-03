import re

def read_input(path):
    with open(path) as f:
        str = ""
        lines = f.readlines()
        for l in lines:
            str += l
    return str

def part_one(input):
    muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input)
    ans = 0
    for mul in muls:
        c1 = int(re.findall(r'\d{1,3},', mul)[0].replace(",",""))
        c2 = int(re.findall(r',\d{1,3}', mul)[0].replace(",",""))

        ans += c1*c2

    return ans

def part_two(input):
    do_str = ""
    # Split the strings at the don't()s and add the first element to the so string
    splt_dont = re.split(r'don\'t\(\)', input)
    do_str+= splt_dont.pop(0)

    # Split the string at the do()s and add second element to do string
    for str in splt_dont:
        splt = re.split(r'do\(\)', str)
        if len(splt) == 1:
            continue
        for s in splt[1:]:
            do_str += s
    return part_one(do_str)

path = r"Day_3\input.txt"
line = read_input(path)

print(part_two(line))