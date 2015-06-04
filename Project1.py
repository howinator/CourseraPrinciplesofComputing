"""
Merge function for 2048 game
"""


def merge(line):
    """
    Function that merges a single row or column in 2048.
    :param line:
    :return:
    """

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
    Function that slides numbers over to the left
    :param line:
    :return:
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


def test():

    test_list = [3, 0, 2, 2, 0]
    print(merge(test_list), "END OF FIRST TEST\n")

    test_list = [3, 0, 2, 2, 0, 2, 2]
    print(merge(test_list), "END OF SECOND TEST\n")

    test_list = [8, 8]
    print(merge(test_list), "END OF THIRD TEST\n")

    test_list = [4]
    print(merge(test_list), "END OF FOURTH TEST\n")

    test_list = [8, 4]
    print(merge(test_list), "END OF FIFTH TEST\n")

    test_list = [4, 4, 8]
    print(merge(test_list), "END OF SIXTH TEST\n")

    test_list = [8, 0, 8]
    print(merge(test_list), "END OF 7th TEST\n")


test()
