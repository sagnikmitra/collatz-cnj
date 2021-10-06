def collatz(number):
    if number % 2 == 0:
        print(number // 2)              # logically, floor division is equivalent to division when even number with 2
        return number // 2
    elif number % 2 != 0:
        print(number * 3 + 1)
        return number * 3 + 1


number = int(input("Please enter a number\n"))
result = collatz(number)                # this way the program also takes 1 as input
while result != 1:
    result = collatz(result)
