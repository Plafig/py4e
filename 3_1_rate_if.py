hours = input('Enter Hours ')
try :
    hours = float(hours)
    rate = input('Enter Rate ')
    rate = float(rate)
    if hours > 40:
        pay = (hours - 40) * 1.5 * rate + 40 * rate
    else:
        pay = hours * rate
    print(pay)
except:
    print("Error, please enter numeric input")
