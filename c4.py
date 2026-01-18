import math

def is_prime(number):
    # 1. Prime numbers are natural numbers greater than 1.
    #    Numbers less than or equal to 1 are not prime.
    if number <= 1:
        return False

    # 2. 2 is the only even prime number.
    if number == 2:
        return True

    # 3. All other even numbers greater than 2 are not prime.
    if number % 2 == 0:
        return False

    # 4. For odd numbers, we check for divisibility by odd numbers
    #    starting from 3 up to the square root of the number.
    #    If a number has a divisor, it must have one less than or equal to its square root.
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    # 5. If no divisors are found, the number is prime.
    return True

# Example usage:
print(f"Is 1 prime? {is_prime(1)}")      # Expected: False
print(f"Is 2 prime? {is_prime(2)}")      # Expected: True
print(f"Is 7 prime? {is_prime(7)}")      # Expected: True
print(f"Is 10 prime? {is_prime(10)}")    # Expected: False
print(f"Is 11 prime? {is_prime(11)}")    # Expected: True
print(f"Is 29 prime? {is_prime(29)}")    # Expected: True
print(f"Is 30 prime? {is_prime(30)}")    # Expected: False
print(f"Is 97 prime? {is_prime(97)}")    # Expected: True