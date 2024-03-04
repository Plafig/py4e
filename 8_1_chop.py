#Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None
def chop(l):
    if len(l) >= 2:
        del l[0]
        del l[-1]
    else:
        l.clear()
    return None

k = [5, 2, 5, 4]
m = k[:]
print(chop(k))
print(k)
print(m)