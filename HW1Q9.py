def appendsums(lst):
    for i in range(25):
        threesum = lst[-1] + lst[-2] + lst[-3]
        lst.append(threesum)
def main():
    sum_three = [0, 1, 2]
    appendsums(sum_three)
    print(sum_three[20])

main()
