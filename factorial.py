def factorial(n:int)->int:
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