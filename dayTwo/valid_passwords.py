def star(fp, isFirst):
    totalcount = 0
    for line in fp:
        info = line.strip().split(" ")
        numbers = info[0].split("-")
        min = int(numbers[0])
        max = int(numbers[1])
        letter = info[1].split(":")[0]
        string = info[2]
        count = 0
        if isFirst == True:
            for i in string:
                if i == letter:
                    count = count + 1
            if min <= count and count <= max:
                totalcount = totalcount + 1
        else:
            if string[min-1] == letter:
                count = count + 1
            if string[max-1] == letter:
                count = count + 1
            if count == 1:
                totalcount = totalcount + 1
    print("Total count is {0}".format(totalcount))

def open_file(file):
    fp = open(file, 'r')
    star(fp, True)
    fp.close()
    fp = open(file, 'r')
    star(fp, False)
    fp.close()

if __name__ == "__main__":
    open_file("./input.txt")