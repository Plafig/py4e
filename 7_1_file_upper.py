#Write a program to read through a file and print the contents of the file (line by line) all in upper case.
def opener() :
    fhand = open('mbox-short.txt')
    for line in fhand:
        print(line.upper())
opener()