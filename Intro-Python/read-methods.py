with open("testing.txt", "w+") as file:
    file.write("Testing, testing, testing")
    file.seek(0)
    print(file.readline())

    #can choose how many characters you'd like to read
    with open("testing.txt", "r") as file:
        print(file.read(5))

    #can read line for reading single line
    with open("testing.txt", "r") as file:
        print(file.readline())

    with open("test.txt", "r") as file:
        print(file.readlines())