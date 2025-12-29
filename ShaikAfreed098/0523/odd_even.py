def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(check_odd_even(number))
