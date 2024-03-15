brackets = [18200, 45000, 135000, 190000]
rates = [0.16, 0.3, 0.37, 0.45]
lumps = [0, 4288, 31288, 51638] # extra 0 so that lump[3] lines up with the amount for bracket[3]
medicare = 0.02

def calc_tax(taxincome):
    if taxincome > brackets[3]: # > 190k
        tax = (taxincome - brackets[3]) * rates[3] + lumps[3]

    elif taxincome > brackets[2]: # > 135k but less than 190k
        tax = (taxincome - brackets[2]) * rates[2] + lumps[2]

    elif taxincome > brackets[1]: # > 45k less than 135k
        tax = (taxincome - brackets[1]) * rates[1] + lumps[1]

    elif taxincome > brackets[0]: # > 18200 less than 45k
        tax = (taxincome - brackets[0]) * rates[0]

    else: # tax free
        tax = 0

    finaltax = tax + (taxincome * medicare)
    return finaltax


def main():
    print("Updated for the 1st July 2024 Tax Cuts")
    print("This calculator only applies to self employed people or people whose employer does not already take out tax \n")

    income = int(input("How much did you earn last year? "))
    writeoff = int(input("How much was your tax offset? "))

    taxincome = income - writeoff
    tax = calc_tax(taxincome)

    print("Your tax owed is", "$" + str(tax))


if __name__ == "__main__":
    main()
