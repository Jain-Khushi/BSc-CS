try:
    file1 = open("file1.txt", "w")  # Firstly create file1 and write some lines in it
    file1.write("Hello\ngood\nto\nsee\nyou")
    file1 = open("file1.txt", "r")  # open file1 in read mode
    file2 = open("file2.txt", "w")  # open file2 in write mode
    lines = file1.readlines()  # read line by line data from file1
    type(lines)
    for i in range(0, len(lines)):
        if i % 2 == 0:  # lines should be the odd numbered lines
            file2.write(lines[i])  # write alternative lines in file2

    file1.close()
    file2.close()

    file1 = open("file1.txt", "r")
    file2 = open("file2.txt", "r")

    print("Content of file1: ")
    print(file1.read())  # print content of file1

    print("\nContent of file2:")
    print(file2.read())

    file1.close()
    file2.close()
except FileNotFoundError:
    print("!!!File not found!!!")
