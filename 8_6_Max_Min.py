numlist = list()
while True:
    numbers = input("Enter a number: ")
    if numbers == 'done':
        break
    try:
        numbers = int(numbers)
        numlist.append(numbers)
    except:
        print("Input should be numbers")



print('Maximum: ', max(numlist))
print('Minimum: ', min(numlist))

