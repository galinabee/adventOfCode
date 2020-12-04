with open("input.txt") as file:
    # clear out the line and place into a list
    input = [line.strip() for line in file]

def partOne(right, down):
    x = 0
    length = len(input[0]) - 1
    trees_hit = 0
    for line in input:
        if line[x] == '#':
            trees_hit += down
        x += right
        x %= length
    return trees_hit

if __name__ == "__main__":
    print("We've hit this many trees: {0}".format(partOne(3, 1)))    