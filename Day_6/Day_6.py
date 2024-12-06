import numpy as np
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
from functools import partial

def read_input(path):
    with open(path) as f:
        # Read lines and remove newlines
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.strip('\n')
            lines[i] = line
        # Initialize grids
        n_rows = len(lines)
        n_cols = len(lines[0])
        obstacales = np.zeros((n_cols, n_rows))
        visited = np.zeros_like(obstacales)

        for row, complete_row in enumerate(lines):
            for column, char in enumerate(complete_row):
                if char == ".":
                    continue
                elif char == "#":
                    obstacales[row, column]  = 1
                else:
                    start_location = np.array([row, column])
                    visited[row, column]  = 1
                    if char == "^":
                        direction = np.array([-1,0])
                    elif char == "v" or char == "V":
                        direction = np.array([1,0])
                    elif char == ">":
                        direction = np.array([0,1])
                    elif char == "<":
                        direction = np.array([0,-1])

    return obstacales, visited, start_location, direction

def rotate_90(direction):
    new_direction = np.array([direction[1], -direction[0]])
    return new_direction

def next_obstacle(current_location, obstacles, visited, direction):
    check_location = current_location
    # Start looking out until the next obstacle
    while obstacles[check_location[0], check_location[1]] == 0:
        visited[check_location[0], check_location[1]] = 1
        check_location = check_location+direction

        # Stopping condition
        dim = obstacles.shape[0]
        if any(check_location >= dim) or any(check_location<0):
            return False, visited, (-1,-1), (-1, -1)

    new_location = check_location-direction
    new_direction = rotate_90(direction)
    return True, visited, new_direction, new_location

def part_one(obstacles, visited, start_location, direction):
    current_location = start_location
    Not_finished = True
    while Not_finished:
        Not_finished, visited, direction, current_location  = next_obstacle(current_location, obstacles, visited, direction)

    ans = int(np.sum(visited))
    return ans, visited

def check_loop(obstacles, visited, start_location, direction):
    current_location = start_location
    lookup_list = []
    Not_finished = True
    while Not_finished:
        Not_finished, visited, direction, current_location  = next_obstacle(current_location, obstacles, visited, direction)
        lu = ''
        for num in [current_location[0], current_location[1], direction[0], direction[1]]:
            lu += str(num)+','
        if lu in lookup_list:
            return True
        else:
            lookup_list.append(lu)
    return False

def part_two(obstacles, visited, start_location, direction, visited_old):
    ans = 0
    found_loops = []
    for i in tqdm(range(obstacles.shape[0])):
        for j in tqdm(range(obstacles.shape[1]), leave=False):
            if obstacles[i,j] == 1 or visited_old[i,j]==0:
                continue
            else:
                temp_obstacles = obstacles.copy()
                temp_visited = visited.copy()
                temp_direction = direction.copy()
                temp_obstacles[i,j] = 1
                if check_loop(temp_obstacles, temp_visited, start_location, temp_direction):
                    found_loops.append((i,j))
                    ans += 1
    return ans


path = r'Day_6\input.txt'
obstacles, visited, start_location, direction = read_input(path)

ans1, visited_old = part_one(obstacles, visited, start_location, direction)
print("Ans 1:", ans1)
ans2 = part_two(obstacles, visited, start_location, direction, visited_old)
print("Ans 2: ", ans2)






