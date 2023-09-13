def main():
    maximumLinesToRead = 5
    linesRead = 0

    userFileName = input("Please enter name of a file: ")

    print()

    readFile = open(userFileName, "r")

    line = readFile.readline()
    linesRead = linesRead + 1

    while line != "" and linesRead <= maximumLinesToRead:
        print(line.restrip("\n"))
        line = readFile.readline()
        linesRead = linesRead + 1

    readFile.close()

main()
