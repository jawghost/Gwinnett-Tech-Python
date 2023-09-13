def main():
    try:
        namesFile = open("names.txt", "r")
    except Exception as exceptionThrown:
        print("There was a problem opening the file:", exceptionThrown)
    else:
        line = namesFile.readline()
        numberOfLines = 0

    while line != "":
        numberOfLines = numberOfLines + 1
        line = namesFile.readline()

    print("The file has", numberOfLines, "line(s)")

main()
