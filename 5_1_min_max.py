def funct() :
    sum = None
    count = 0
    max = None
    min = None
    while True :
        num = input("Please enter number: ")
        try :
            num = int(num)
        except :
            print("bad data")
        if num == "done":
            break
# Def sum
        if sum is None:
            sum = num
        else :
            sum = sum + num
# Def max
        if max is None :
            max = num
        elif num > max :
            max = num
# Def min
        if min is None :
            min = num
        elif num < min :
            min = num
        count = count + 1
        av = sum / count

    print(sum, count, av, max, min)
funct()
