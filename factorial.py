def calculate_factorial(num: int) -> int:
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


def main() -> None:
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise ValueError("Negative numbers are not allowed")
    except ValueError:
        print("Please enter a valid number")
        exit()

    print(calculate_factorial(num))


if __name__ == "__main__":
    main()
