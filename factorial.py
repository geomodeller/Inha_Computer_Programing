def factorial(n:int)->int:
    """
    Calculates the factorial of a given integer n.

    Args:
        n (int): The given integer.

    Returns:
        int: The factorial of n.

    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is negative.

    Examples:
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(5)
        120
    """
    if not isinstance(n, int):
        raise TypeError(f'Input should be integer - current input = {type(n)}')
    elif n < 0:
        raise ValueError('Input should be 0 or positive')

    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

# define function to comupte n-th fibonacci sequence
def fibonacci(n:int)->int:
    if n == 0 or n == 1:
        return 1
    return  fibonacci(n-1) + fibonacci(n-2)

# define function to get sum of elements in a list
def sum_list(lst:list)->int:
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])

# define function to calculate sum of fibonacci sequence upto n-th number
def sum_fibonacci(n:int)->int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + sum_fibonacci(n-1)

if __name__ == '__main__':
    print(help(factorial))