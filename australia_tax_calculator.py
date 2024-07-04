BRACKETS = [18200, 45000, 135000, 190000]
RATES = [0.16, 0.3, 0.37, 0.45]
# total ammount paid at each bracket, LUMPS[0] is the total paid between BRACKETS[0] and BRACKETS[1] etc.
LUMPS = [4288, 31288, 51638]
MEDICARE_RATE = 0.02
MEDICARE_THRESHOLD = 32500


def calc_tax(income: int) -> int:
    tax = 0.0
    if income > BRACKETS[3]:
        tax = (income - BRACKETS[3]) * RATES[3] + LUMPS[2]

    elif income > BRACKETS[2]:
        tax = (income - BRACKETS[2]) * RATES[2] + LUMPS[1]

    elif income > BRACKETS[1]:
        tax = (income - BRACKETS[1]) * RATES[1] + LUMPS[0]

    elif income > BRACKETS[0]:
        tax = (income - BRACKETS[0]) * RATES[0]

    # can pay tax but still not pay medicare levy as medicare threshold > tax free threshold
    if income > MEDICARE_THRESHOLD:
        tax += income * MEDICARE_RATE

    return int(tax)


def get_income() -> int:
    try:
        income = int(input("What is your taxable income? "))
    except ValueError:
        print("Enter a Valid Number\n")
        return get_income()
    return income


def main() -> None:
    print(
        "Updated for the 1st July 2024 Tax Cuts\nThis calculator only applies to Individual Australian Residents\nThis is only an estimate, even government websites get estimated tax wrong\n"
    )

    print(f"Tax Owed: ${calc_tax(get_income())}")


if __name__ == "__main__":
    main()
