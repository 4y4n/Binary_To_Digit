def binary_to_decimal():
    binary = int(input("Please enter the binary number: "))
    digits = [int(x) for x in str(binary)]
    exponents = (len(digits)) - 1
    decimal = 0
    for char in digits:
        if char == 1:
            decimal += 2**exponents
        exponents -= 1
    print(decimal)


def decimal_to_binary():
    digit = int(input("Please enter the decimal number: "))
    power = 1
    exponents = 0
    while power * 2 <= digit:
        power = power * 2
        exponents += 1
    binary = 0
    for i in range(0, exponents+1):
        if power <= digit:
            binary += 10**(exponents-i)
            digit -= power
        power = power / 2
    print(binary)


Continue = "y"
while Continue == "y" or Continue == "Y" or  Continue == "yes" or Continue == "Yes":
    inp = str(input("Which type would you like to start with?(Binary/Decimal): "))
    if inp == "binary" or inp == "Binary" or inp == "b" or inp == "B":
        binary_to_decimal()
    elif inp == "decimal" or inp == "Decimal" or inp == "d" or inp == "D":
        decimal_to_binary()
    Continue = str(input("Would you like to continue?(Yes/No): "))
