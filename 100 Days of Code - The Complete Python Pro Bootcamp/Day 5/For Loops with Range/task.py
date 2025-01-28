sum = 0
for number in range(1,101):
    sum += 1
    if sum % 3 == 0 and sum % 5 == 0:
        print("FizzBuzz")
    elif sum % 3 == 0 :
        print("Fizz")
    elif sum % 5 == 0:
        print("Buzz")
    else :
        print(sum)
