import random

prime = []
nonprime = []

for i in range(10):
    num = random.randint(i, 1000)
    if num > 1:
        for x in range(2, num):
            if (num % x) == 0:
                nonprime.append(str(num) + " (" + str(i) + u"\u00D7" + str(num // x) + ")")
                break
        else:
            prime.append(num)
    else:
        nonprime.append(num)

prime.sort()
nonprime.sort()

prime_new = [str(a) for a in prime]
nonprime_new = [str(a) for a in nonprime]

if len(prime) == 0:
    print("No Prime Numbers")
else:
    print("Prime Numbers:", ", ". join(prime_new))

if len(nonprime) == 0:
    print("No Non Prime Numbers")
else:
    print("Non Prime Numbers:", ", ". join(nonprime_new))