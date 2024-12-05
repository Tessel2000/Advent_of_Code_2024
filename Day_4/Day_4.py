def read_input(path):
    with open(path) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            ln = line.replace("\n","")
            lines[i] = ln
    return lines

def find_X(lines):
    Xes = []
    for j, line in enumerate(lines):
        ind = [i for i, ltr in enumerate(line) if ltr == "X"]
        for i in ind:
            Xes.append((j,i))
    return Xes

def find_M(lines, x, dim):
    # Check for Ms
    M_dirs = []
    for i in [-1, 0, 1]:
        x_ind = x[0] + i
        if x_ind>=0 and x_ind<dim:
            for j in [-1, 0, 1]:
                y_ind = x[1]+j
                if y_ind>=0 and y_ind<dim:
                    if lines[x_ind][y_ind] == "M":
                        M = [(x_ind, y_ind), (i,j)]
                        M_dirs.append(M)
    return M_dirs

def check_surroundings(loc, lines, check_char, direction):
    max = len(lines)-1
    check_lock = [loc[i]+direction[i] for i in range(len(loc))]
    if all(i>=0 and i<=max for i in check_lock) and check_char in str(lines[check_lock[0]][check_lock[1]]):
        return True
    else:
        return False

def part_one(lines):
    ans = 0 

    X = find_X(lines)
    dim = len(lines[0])
    for x in X:
        M = find_M(lines, x, dim)
        for m in M:
            loc = m[0]
            dir = m[1]
            
            if not check_surroundings(loc, lines, 'A', dir):
                continue
            
            loc = [loc[0]+dir[0], loc[1]+dir[1]]
            if not all(i>=0 and i<=dim-1 for i in loc):
                continue
            if not check_surroundings(loc, lines, 'S', dir):
                continue
            
            ans+=1
    return ans

def extract_square(lines, loc):
    str = ""
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            x_ind = loc[0]+i
            y_ind = loc[1]+j
            if not all(p>=0 and p<=len(lines[0])-1 for p in [x_ind, y_ind]):
                raise ValueError("The given lock is at the edge of the grid and therefore will not produce a square")
            str += lines[x_ind][y_ind]
    return str

def check_square(square):
    if not square[4]=="A":
        return False
    elif not ((square[0]=="M" and square[8]=="S") or (square[0]=="S" and square[8]=="M")):
        return False
    elif not ((square[2]=="M" and square[6]=="S") or (square[2]=="S" and square[6]=="M")):
        return False
    else: return True

def part_two(lines):
    ans = 0
    dim = len(lines[0])
    for i in range(1,dim-1):
        for j in range(1,dim-1):
            square = extract_square(lines, (i,j))
            if check_square(square):
                ans += 1
    return ans

path = r'Day_4\input.txt'
lines = read_input(path)
print("Answer part 1: ", part_one(lines))
print("Answer part 2: ", part_two(lines))