def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    return result


try:
    print("Enter a number")
    num = int(input())
    while True:
        resolve = collatz(num)
        num = resolve
        print(resolve)
        if resolve == 1:
            print("It works!")
            break
except ValueError as e:
    print("Please input a valid integer!")
