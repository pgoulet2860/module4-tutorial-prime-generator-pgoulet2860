"""
prime_generator.py

pwd
Prime factors generator using a generator construct
"""
def prime_factors(number):
    """ Prime Factor implemented as a generator """
    if (isinstance(number, int) is False) or (number < 1):
        raise ValueError

    factor = 2 # initial candidate for a factor
    while factor <= number:
        while number % factor == 0: # while number exactly divisible by factor
                                    # reduce number by it and yield factor
            number = round(number/factor)
            yield factor
        factor += 1 # then, consider next integer as a factor
