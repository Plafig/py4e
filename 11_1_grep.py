import re
ls = []
def grep(reg):
    fhand = open("mbox.txt")
    for line in fhand:
        text = re.findall(reg, line)
        if len(text) > 0:
            ls.append(text)
reg = input("Enter a regular expression: ")
grep(reg)
print('mbox.txt had', len(ls), 'lines that matched', reg)