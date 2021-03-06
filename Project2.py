"""
Clone of 2048 game.
"""
import random
import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    merged_list = slide_over(line)

    length_initial = len(line)

    for index in range(length_initial - 1):
        if merged_list[index] == merged_list[index + 1]:
            merged_list[index] *= 2
            merged_list[index + 1] = 0

    merged_list = slide_over(merged_list)

    return merged_list


def slide_over(line):
    """
    Function that slides numbers over to the left, a helper function for merge
    """
    fixed_line = []
    num_zeros = 0

    for num in line:
        if num != 0:
            fixed_line.append(num)
        else:
            num_zeros += 1

    for zero in range(num_zeros):
        fixed_line.append(0)

    return fixed_line


class TwentyFortyEight(object):
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):

        self.height = grid_height
        self.width = grid_width
        self.grid = []
        self.reset()

        # populate initial tiles dictionary
        self.initial_tiles = {}
        up_list = [(0, col) for col in range(0, self.width)]
        down_list = [(self.height - 1, col) for col in range(0, self.width)]
        left_list = [(row, 0) for row in range(0, self.height)]
        right_list = [(row, self.width - 1) for row in range(0, self.height)]
        self.initial_tiles[UP] = up_list
        self.initial_tiles[DOWN] = down_list
        self.initial_tiles[LEFT] = left_list
        self.initial_tiles[RIGHT] = right_list

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for dummy_col in range(self.width)] for dummy_row in range(self.height)]
        self.new_tile()
        self.new_tile()

        pass

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """

        temp_row = []
        str_grid = ""
        for row in self.grid:
            for col in row:
                temp_row.append(col)
            row_str = str(temp_row) + "\n"
            str_grid += row_str
            temp_row = []

        return str_grid

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        is_grid_changed = False

        # Since the grid can be rectangular you must distinguish between moving up and down vs. left and right
        if direction == UP or direction == DOWN:
            for init_coord_pair in self.initial_tiles[direction]:
                temp_list_coords = []
                # build list of coordinates based on initial coordinates and offset
                for row in range(self.height):
                    temp_list_coords.append((init_coord_pair[0] + OFFSETS[direction][0] * row, init_coord_pair[1]))

                values = self.form_line_from_coords(temp_list_coords)
                merged_values = merge(values)

                # test if merged values are different than original values
                if merged_values != values:
                    is_grid_changed = True

                # update values in grid
                for row in range(self.height):
                    self.grid[row][init_coord_pair[1]] = merged_values[row]

        elif direction == LEFT or direction == RIGHT:
            for init_coord_pair in self.initial_tiles[direction]:
                temp_list_coords = []
                for col in range(self.width):
                    temp_list_coords.append((init_coord_pair[0], init_coord_pair[1] + OFFSETS[direction][1] * col))

                values = self.form_line_from_coords(temp_list_coords)
                merged_values = merge(values)

                # test if merged_values are different than original values
                if merged_values != values:
                    is_grid_changed = True

                # update values in grid
                for col in range(self.width):
                    self.grid[init_coord_pair[0]][col] = merged_values[col]

        if is_grid_changed:
            self.new_tile()

        pass

    def traverse_grid(self, start_cell, direction, num_steps):
        """
        This function traverses the grid and returns values from the grid for
        the row or colum values
        """
        values = []
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + start_cell * direction[1]
            values.append()



    def form_line_from_coords(self, list_coords):
        """
        This function takes in a list of coordinates (as tuples) and returns the values at those coordinates
        """
        values = []
        for coord in list_coords:
            values.append(self.grid[coord[0]][coord[1]])

        return values

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        
        # Keep choosing cell until you get an empty, zero cell
        # if the cell is empty change the flag and exit the loop
        is_cell_occupied = True
        while is_cell_occupied:
            rand_row = random.randint(0, self.height - 1)
            rand_col = random.randint(0, self.width - 1)
            if self.grid[rand_row][rand_col] == 0:
                is_cell_occupied = False

        rand_two_or_four = random.random()
        two_upper_limit = .9
        if rand_two_or_four < two_upper_limit:
            self.grid[rand_row][rand_col] = 2
        elif rand_two_or_four >= two_upper_limit:
            self.grid[rand_row][rand_col] = 4

        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def print_direction_dict(self):
        """
        Tests if the initial tiles dict was set up properly
        """
        print(self.initial_tiles)
        pass

x = TwentyFortyEight(4, 4)
print(str(x))
x.move(LEFT)

#y = TwentyFortyEight(5, 4)
#print(str(y))

#z = TwentyFortyEight(8, 2)
#print(str(z))


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

