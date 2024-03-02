#. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

fhand = open("mbox-short.txt")
t = {}
for line in fhand:
    if not line.startswith("From "): continue
    line = line.strip()
    words = line.split()
    time = words[5].split(":")[0]
    #print("Debug ", time)
    t[time] = t.get(time, 0) + 1

srtd = sorted([(k, v) for (k, v) in t.items()])

for k,v in srtd:
    print(k, v)