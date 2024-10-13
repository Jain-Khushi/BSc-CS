def isPrime(n, i = 2):
 
    # Base cases
    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
 
    # Check for next divisor
    return isPrime(n, i + 1)
 
 
# Driver Program
n = 20
if (isPrime(n)):
    print("It is a prime number.")
else:
    print("It is not a prime number.")
