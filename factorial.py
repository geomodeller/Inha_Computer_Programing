def factorial(n:int)->int:
    """숫자의 factorial을 구하는 함수

    Args:
        n (int): factorial할 숫자

    Raises:
        TypeError: input이 int여야 함
        ValueError: input이 0이거나 양수여야 함

    Returns:
        int: factorial
    """
    if not isinstance(n, int):
        raise TypeError(f'Input should be integer - current input = {type(n)}')
    elif n < 0:
        raise ValueError('Input should be 0 or positive')

    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)



if __name__ == '__main__':
    print(help(factorial))