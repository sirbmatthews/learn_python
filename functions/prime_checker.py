def prime_checker(number):
    """Returns True if a given argument is a Prime number or False if it is not a Prime number."""
    is_prime = True
    for num in range(2, number):
        if num < number and number % num == 0:
            is_prime = False
            break
        else:
            is_prime = True 

    return is_prime
