# fizz, if divisible by 3
# buzz, if divisible by 5
# fizzbuzz, if divisible by 15
# if not divisible return number

def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    else:
        return number


number = int(input("Enter the number: "))
print(fizz_buzz(number))
