"""
Merge function for 2048 game
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    :param line:
    :return:
    """
    slid_over_list = []
    index_is_zero = []

    length_initial = len(line)

    if length_initial == 1:
        slid_over_list.append(line[0])
        return slid_over_list

    if length_initial == 2:
        if line[0] == line[1]:
            slid_over_list.append(line[0] * 2)
            slid_over_list.append(0)
        elif line[1] > line[0]:
            slid_over_list.append(line[1])
            slid_over_list.append(line[0])
        else:
            slid_over_list.append(line[0])
            slid_over_list.append(line[1])
        return slid_over_list

    for num1 in range(length_initial):
        key = line[num1]



        for num2 in range(num1 + 1, length_initial):
            comparing_key = line[num2]
            if (key != comparing_key and comparing_key != 0 and key != 0):
                slid_over_list.append(key)
                print("1ST BREAK", "num1 =", num1, "num2 =", num2)
                print(slid_over_list)
                print('\n')


                break
            elif (key == comparing_key and num2 not in index_is_zero and key != 0):
                slid_over_list.append(key * 2)
                index_is_zero.append(num2 + 1)
                print("2nd BREAK", "num1 =", num1, "num2 =", num2)
                print(slid_over_list)
                print('\n')


                break

    num_zeros = length_initial - len(slid_over_list)

    zero_counter = 0

    while zero_counter < num_zeros:
        slid_over_list.append(0)
        zero_counter += 1

    #print("1ST BREAK", "num1 =", num1, "num2 =", num2)
    #print(slid_over_list)
    #print('\n')
    #print("2nd BREAK", "num1 =", num1, "num2 =", num2)
    #print(slid_over_list)
    #print('\n')

    return slid_over_list



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




test()
