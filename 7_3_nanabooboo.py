#Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

def textfile() :
    count = 0
    summ = 0
    filename = input("Enter file name ")
    if filename == "na na boo boo" :
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    try:
        fhand = open(filename)
    except:
        print('File cannot be opened:', filename)
        exit()
    for line in fhand :
        if line.startswith('X-DSPAM-Confidence') :
            line = line.rstrip()
            start = line.find(' ')
            num = line[start:]
            num = float(num)
            summ = summ + num
            count = count + 1
        else:
            continue
        print(line)
    print(count, summ, summ / count)
textfile()