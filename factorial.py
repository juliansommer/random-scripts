def calculate_factorial(num: int) -> int:
    if num > 1:
        return num * calculate_factorial(num - 1)
    return 1


def main() -> None:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number")
        exit()

    print(calculate_factorial(num))


if __name__ == "__main__":
    main()
