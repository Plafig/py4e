num = input('Please enter number ')
try:
    num = float(num)
    if num >= 0.9 :
        print("A")
    elif num >= 0.8 :
        print("B")
    elif num >= 0.7 :
        print("C")
    elif num >= 0.6 :
        print("D")
    elif num < 0.6 :
        print("F")
except :
    print("Bad score")