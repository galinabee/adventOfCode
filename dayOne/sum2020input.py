import os

def populate_from_file():
    fp = open('./dayOne/sum2020input.txt', 'r')
    input_set = set(int(line.strip()) for line in fp)
    fp.close()
    return input_set

def find_two_values(input_set):
    for val in input_set:
        if 2020-val in input_set:
            return [val, 2020-val]

def find_three_values(input_set):
    for val1 in input_set:
        for val2 in input_set:
            if 2020-val1-val2 in input_set:
                return [val1, val2, 2020-val1-val2]

def multiply_list_values(input_list):
    product = 1
    for val in input_list:
        product *= val
    return product

def main():
    print(os.getcwd())
    input_set = populate_from_file()
    value_list = find_two_values(input_set)
    print("The two values are {0} and {1}".format(value_list[0], value_list[1]))
    print("Multiplying the two is {0}".format(multiply_list_values(value_list)))

    value_list = find_three_values(input_set)
    print("The three values are {0}, {1} and {2}".format(value_list[0], value_list[1], value_list[2]))
    print("Multiplying the three is {0}".format(multiply_list_values(value_list)))

# The two values are 1124 and 896
# Multiplying the two is 1007104
# The three values are 24, 539 and 1457
# Multiplying the three is 18847752

if __name__ == "__main__":
    main()