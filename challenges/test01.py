# To convert the enter number into their words

# input 123456
# output one two three four five six

mydict = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five",
          '6': "six", '7': "seven", '8': "eight", '9': "nine", '0': "zero", }


def to_names(number):
    result = ""
    for num in number:
        result = result + " " + mydict.get(num)
    return result


number = input("Enter the number: ")
print(to_names(number))
