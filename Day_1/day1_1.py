def read_input(file_path):
    lst1 = []
    lst2 = []
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            line = line.split('   ')
            c1 = int(line[0])
            c2 = int(line[1])
            lst1.append(c1)
            lst2.append(c2)
    return lst1, lst2

def part_1(l1, l2):
    l1.sort()
    l2.sort()

    ans = 0
    for i in range(len(l1)):
        a = abs(l1[i]-l2[i])
        ans += a
    return ans

def part_2(l1,l2):
    score = 0
    dict_unique = {}

    for num in list1:
        if num in dict_unique.keys():
            score += dict_unique[num]
        else:
            c = l2.count(num)
            score += num*c
            dict_unique[num] = score
    return score

path = r"C:\Users\tesse\Advent_of_Code_2024\Day_1\input.txt"
list1, list2 = read_input(path)

ans = part_2(list1, list2)
print(ans)