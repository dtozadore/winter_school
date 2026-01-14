

# Setting the mesh map
map_grid = [[0 for _ in range(3)] for _ in range(3)]



map = [[0,0,0],[1,1,1],[0,0,0]]

map[1][0]

print("map", map[1][0])

exit()

# Filling with the obstacles
for i in range(3):
    map_grid[i][1] = 1

# Inserting the robot
robot_position = [1, 1]  # Python uses 0-based indexing, so [2,2] in MATLAB becomes [1,1]


# computational cost counter
comp_cost = 0







# Display the map
def print_map(map_to_print, robot_position):
    # Create a copy so we don't overwrite the original map
    temp_map = [row[:] for row in map_to_print]
    temp_map[robot_position[0]][robot_position[1]] = 2
    for row in temp_map:
        print(row)
    print()


print("Before inserting the robot")
print_map(map_grid, robot_position)

print("After inserting the robot")
print_map(map_grid, robot_position)


# Function to check whether the cell is a valid cell to move
def is_cell_valid(cell_value):
    return cell_value == 0  # Valid if cell is empty (0)


# Implementing the move function
def move(direction_to_move, current_position, current_map):
    new_position = current_position[:]

    if direction_to_move == "left":
        candidate = [current_position[0], current_position[1] - 1]
        if candidate[1] >= 0 and is_cell_valid(current_map[candidate[0]][candidate[1]]):
            new_position = candidate
        else:
            print("Invalid move or obstacle encountered.")

    elif direction_to_move == "right":
        candidate = [current_position[0], current_position[1] + 1]
        if candidate[1] < len(current_map[0]) and is_cell_valid(current_map[candidate[0]][candidate[1]]):
            new_position = candidate
        else:
            print("Invalid move or obstacle encountered.")

    elif direction_to_move == "up":
        candidate = [current_position[0] - 1, current_position[1]]
        if candidate[0] >= 0 and is_cell_valid(current_map[candidate[0]][candidate[1]]):
            new_position = candidate
        else:
            print("Invalid move or obstacle encountered.")

    elif direction_to_move == "down":
        candidate = [current_position[0] + 1, current_position[1]]
        if candidate[0] < len(current_map) and is_cell_valid(current_map[candidate[0]][candidate[1]]):
            new_position = candidate
        else:
            print("Invalid move or obstacle encountered.")

    else:
        print("Direction not recognized")

    return new_position


# Test moves
robot_position = move("up", robot_position, map_grid)
print("After moving the robot up:")
print_map(map_grid, robot_position)

robot_position = move("left", robot_position, map_grid)
print("After moving the robot left:")
print_map(map_grid, robot_position)





# matrix=[[ 0  4  0  0  0  0  0  8  0]
#  [ 4  0  8  0  0  0  0 11  0]
#  [ 0  8  0  7  0  4  0  0  2]
#  [ 0  0  7  0  9 14  0  0  0]
#  [ 0  0  0  9  0 10  0  0  0]
#  [ 0  0  4 14 10  0  2  0  0]
#  [ 0  0  0  0  0  2  0  1  6]
#  [ 8 11  0  0  0  0  1  0  7]
#  [ 0  0  2  0  0  0  6  7  0]]
