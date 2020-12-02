def populate_from_file():
    fp = open('./sum2020input.txt', 'r')
    input_set = set(fp)
    print(input_set)
    fp.close()
    return input_set

def main():
    print("hello")

if __name__ == "__main__":
    main()