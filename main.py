def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

    un bug

if __name__ == '__main__':
    for i in range(1, 101):
        print(
            f"{i:3} | {fizz_buzz(i):10} |"
        )
