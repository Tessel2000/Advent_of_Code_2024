def read_input(path):
    input = []
    with open(path) as f:
        lines = f.readlines()
    for line in lines:
        line = line.replace('\n', "")
        line = line.split(' ')
        line = [int(i) for i in line]
        input.append(line)
    return input
    

def check_report(report):
    broken_conditions = 0
    if report[0] >= report[1]:
        asc = 0
    else:
        asc = 1
    for i in range(len(report)-1):
        r1 = report[i]
        r2 = report[i+1]
        # Check first condition
        if not asc:
            if r1 < r2 or r1 == r2:
                return False
        else:
            if r1>r2 or r1==r2:
                return False
        # Check second condition
        diff = abs(r1-r2)
        if diff > 3 or diff < 1:
            return False

    return True
    
def day_one(input):
    ans = 0
    for i, report in enumerate(input):
        safe = check_report(report)
        if safe:
            ans += 1
        else:
            # Implement problem dampner
            for i in range(len(report)):
                sub_report = [elem for j, elem in enumerate(report) if j!=i]
                safe_sub = check_report(sub_report)
                if safe_sub:
                    ans += 1
                    break
    return ans


path = r"C:\Users\tesse\Advent_of_Code_2024\Day_2\input.txt"
reports = read_input(path)
ans= day_one(reports)
print(ans)