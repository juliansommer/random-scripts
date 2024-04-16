brackets = [18200, 45000, 135000, 190000]
rates = [0.16, 0.3, 0.37, 0.45]
lumps = [4288, 31288, 51638]
medicare = 0.02

def calc_tax(income):
    if income > brackets[3]: # > 190k
        tax = (income - brackets[3]) * rates[3] + lumps[2]

    elif income > brackets[2]: # > 135k but less than 190k
        tax = (income - brackets[2]) * rates[2] + lumps[1]

    elif income > brackets[1]: # > 45k less than 135k
        tax = (income - brackets[1]) * rates[1] + lumps[0]

    elif income > brackets[0]: # > 18200 less than 45k
        tax = (income - brackets[0]) * rates[0]

    else: # tax free
        tax = 0

    return int(tax + (income * medicare))


def main():
    print("Updated for the 1st July 2024 Tax Cuts\nThis calculator only applies to Australian Residents")

    income = int(input("How much did you earn last year? "))
    writeoff = int(input("How much was your tax offset? "))

    print(f"Your tax owed is ${calc_tax(income - writeoff)}")


if __name__ == "__main__":
    main()
