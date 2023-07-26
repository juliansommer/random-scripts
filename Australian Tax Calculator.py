print("This calculator only applies to self employed \
people or people whose employer does not already take out tax \n")

income = int(input("How much did you earn last year? "))
writeoff = int(input("How much was your tax offset? "))
resident = input("Are you an Australian Resident? y/n ")

taxincome = income - writeoff

if resident.lower() == "y":
    if taxincome <= 18200:
        print("You do not have to pay any tax")
    elif taxincome <= 45000:
        tax = 0.19 * (taxincome - 18200)
    elif taxincome >= 45001 and taxincome <= 120000:
        tax = 5092 + (0.325 * (taxincome - 45000))
    elif taxincome >= 120001 and taxincome <= 180000:
        tax = 29467 + (0.37 * (taxincome - 120000))
    elif taxincome >= 180001:
        tax = 51667 + (0.45 * (taxincome - 180000))

if resident.lower() == "n":
    if taxincome <= 120000:
        tax = 0.325 * taxincome
    elif taxincome >= 120001 and taxincome <= 180000:
        tax = 39000 + (0.37 * (taxincome - 120000))
    elif taxincome >= 180001:
        tax = 61200 + (0.45 * (taxincome - 180000))

print("Your tax owed is", "$" + str(tax))
