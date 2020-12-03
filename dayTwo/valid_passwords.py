def populate_from_file():
    fp = open('./input.txt', 'r')
    totalcount = 0
    for line in fp:
        info = line.strip().split(" ")
        
        numbers = info[0].split("-")
        min = int(numbers[0])
        max = int(numbers[1])
        letter = info[1].split(":")[0]
        string = info[2]
        count = 0
        for i in string:
            if i == letter:
                count = count + 1
        if min <= count and count <= max:
            totalcount = totalcount + 1
    fp.close()
    print("Total count is {0}".format(totalcount))
    return totalcount

    #506

def populate_from_file2():
    fp = open('./input.txt', 'r')
    totalcount = 0
    for line in fp:
        info = line.strip().split(" ")
        
        numbers = info[0].split("-")
        min = int(numbers[0])
        max = int(numbers[1])
        letter = info[1].split(":")[0]
        string = info[2]
        count = 0
        if string[min-1] == letter:
            count = count + 1
        if string[max-1] == letter:
            count = count + 1
        if count == 1:
            totalcount = totalcount + 1
    fp.close()
    print("Total count is {0}".format(totalcount))
    return totalcount
    #443

if __name__ == "__main__":
    populate_from_file()
    populate_from_file2()