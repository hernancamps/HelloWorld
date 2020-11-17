import math

def is_prime(number):
    if not isinstance(number, int):
        raise TypeError("You must enter a number.")
    divisor = math.floor(number/2)
    prime = False
    while divisor >= 2 or prime is False:
        if number % divisor == 0:
            prime = True
        divisor -= 1
        
    return prime
