"""
Merge function for 2048 game
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    :param line:
    :return:
    """
    length_initial = len(line)

    slid_over_list = slide_over(line)






def slide_over(line):
    """
    Function that slides numbers over to the left
    :param line:
    :return:
    """
    fixed_line = []
#    num_zeros = 0

    for num in line:
        if num != 0:
            fixed_line.append(num)
#        else:
#            num_zeros += 1

#    for zero in range(num_zeros):
#        fixed_line.append(0)

    return fixed_line

def test():

    test_list = [3, 0, 2, 2, 0]

    print(slide_over(test_list))

test()
