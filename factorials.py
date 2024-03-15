def calculate_factorial(num):
    if num > 1:
       return num * calculate_factorial(num-1)
    return 1


print(calculate_factorial(4))