"""
Clone of 2048 game.
"""

# import poc_2048_gui

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
        # replace with your code
        self.height = grid_height
        self.width = grid_width
        self.grid = []
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for dummy_col in range(self.width)] for dummy_row in range(self.height)]

        pass

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        temp_row = []
        str_grid = ""
        for row in self.grid:
            for col in row:
                temp_row.append(col)
            row_str = str(temp_row) + "\n"
            str_grid += row_str
            temp_row = []

        return str_grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return 0

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return 0

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return 0

x = TwentyFortyEight(4, 4)
print(str(x))


# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

