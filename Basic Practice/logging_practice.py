import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of the Factorial Program!!')

def factorial(n):
    """Compute factorial of n recursively."""
    logging.debug(f'Computing factorial({n})')
    if n < 0:
        logging.error('Factorial is not defined for negative numbers')
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        logging.debug(f'Known Fact: 0! = 1! = 1')
        return 1
    else:
        result = n * factorial(n - 1)
        logging.debug(f'Computed factorial({n}) = {result}')
        return result
    

num = 6
print(f"Calculating factorial of {num}", factorial(num))
logging.debug('End of the Factorial Program!!')