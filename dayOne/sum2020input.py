import os

def populate_from_file():
    print(os.getcwd())
    fp = open('./dayOne/sum2020input.txt', 'r')
    input_set = set(int(line.strip()) for line in fp)
    print(input_set)
    fp.close()
    return input_set

def find_two_values(input_set):
    for val in input_set:
        if 2020-val in input_set:
            return val

def main():
    print(os.getcwd())
    input_set = populate_from_file()
    val = find_two_values(input_set)
    print("The two values are {0} and {1}".format(val, 2020-val))
    print("Multiplying the two is {0}".format((2020-val)*val))

if __name__ == "__main__":
    main()