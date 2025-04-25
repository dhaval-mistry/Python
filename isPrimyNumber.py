number = int(input("Enter a number: "))
is_prime = True;

if(number >1):
    for i in range(2, number):
        if(number % i == 0):
            is_prime = False
            break

print (f"{number} is a prime number" if is_prime else f"{number} is not a prime number")
