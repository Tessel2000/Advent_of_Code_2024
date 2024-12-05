def read_input(path):
    with open(path) as f:
        lines = f.readlines()
        ind = lines.index("\n")
        rules = lines[0:ind]
        rules_return = []
        for rule in rules:
            r = rule.replace("\n", "").split("|")
            rules_return.append(r)
        pages = lines[ind+1:]
        pages_return = []
        for page in pages:
            p = page.replace("\n", "").split(",")
            pages_return.append(p)
        
    return rules_return,pages_return

def check_rule(page, rule):
    if rule[0] in page and rule[1] in page:
        first_ind = page.index(rule[0])
        second_ind = page.index(rule[1])
        if first_ind < second_ind:
            return [True, 0, 0]
        else: return False, first_ind, second_ind
    else:
        return [True,0,0]

def part_one(rules, pages):
    ans = 0 
    for page in pages:
        i = 0
        while check_rule(page, rules[i])[0]:
            i +=1
            if i == len(rules):
                mid = int(page[len(page)//2])
                ans += mid
                break
    return ans

def check_page(page, rules):
    broken_rules = []
    for rule in rules:
        check = check_rule(page, rule)
        if check[0]:
            continue
        broken_rules.append([rule, check[1:]])
    return broken_rules

def swap_entries(page, swap):
    frst_char, scnd_char = (page[swap[0]], page[swap[1]])
    page[swap[0]] = scnd_char
    page[swap[1]] = frst_char
    return page

def part_two(rules, pages):
    ans = 0
    for page in pages:
        broken_rules = check_page(page, rules)
        if len(broken_rules)==0:
            continue
        else:
            # Swap the first 2 for the boken rules
            while len(broken_rules) != 0:
                page = swap_entries(page, broken_rules[0][1])
                broken_rules = check_page(page, rules)
            mid = int(page[len(page)//2])
            ans += mid
    return ans

path = r'Day_5\input.txt'
rules, pages = read_input(path)
ans = part_two(rules, pages)
        
print(ans)