numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number == 0:
        print(f"{number} is Zero")
    else:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
