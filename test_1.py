import re
ls = []
su = 0
fhand = open("mbox.txt")
for line in fhand:
    text = re.findall('^New.+:\s([0-9]+)', line)
    if len(text) > 0:
       #print(text)
        ls.append(text)
print(sum(int(x[0]) for x in ls)/ len(ls))
