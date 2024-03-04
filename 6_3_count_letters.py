#The following program counts the number of times the letter “a” appears in a string:
def count(text, letter):
    number = 0
    for i in text :
        if i == letter :
            number += 1
    print(number)


count('Hello world', 'l')