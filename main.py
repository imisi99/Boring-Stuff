import random

# number = random.randint(1, 20)
# trials = 0
# while trials <= 5:
#     print("I am thinking of a number between 1 and 20 can you guess it?")
#     _input = int(input())
#     trials += 1
#     if _input - number > 5:
#         print("Ah, That's a bit too much!")
#     elif number - _input > 5:
#         print("Woah, that's too low even for me.")
#     elif number == _input:
#         break
#     else:
#         print("Getting there")
# if trials <= 5:
#     print(f"Congratulation on getting the number it took you {trials} trials")
# else:
#     print(f"Sorry the number i was thinking of is {number}")


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    return result


print("Enter a number")
num = int(input())
while True:
    resolve = collatz(num)
    num = resolve
    print(resolve)
    if resolve == 1:
        break
print("It works!")
