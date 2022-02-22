import random


def num_1(input_n: int) -> str:
    even = 0
    odd = 0
    while input_n > 0:
        num = input_n % 10
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        input_n //= 10
    res = f'Четных - {even}, нечетных - {odd}'
    return res


def num_2(input_n: int) -> int:
    res = 0
    while input_n > 0:
        num = input_n % 10
        input_n //= 10
        res = res * 10 + num
    return res


def num_3(input_n: int) -> int:
    res = 0
    f = 1
    for _ in range(input_n):
        res += f
        f /= -2
    return res


def num_4(input_n: int) -> bool:
    res_1 = sum([n + 1 for n in range(input_n)])
    res_2 = input_n * (input_n + 1) / 2
    check = True if res_1 == res_2 else False
    return check


def num_5() -> int:
    arr = int(input('Введите последовательность чисел любой длины подряд без пробелов: '))
    num = int(input('Введите искомую цифру: '))
    res = 0
    while arr > 0:
        buf = arr % 10
        arr //= 10
        if buf == num:
            res += 1
    return res


def num_6(nums: str) -> str:
    num_list = list(map(int, nums.split(',')))
    res_list = [0]*(len(num_list))
    max_pair = [0, 0]
    for i, num in enumerate(num_list):
        while num > 0:
            n = num % 10
            num //= 10
            res_list[i] += n
        if res_list[i] > max_pair[0]:
            max_pair[0] = res_list[i]
            max_pair[1] = i
    return f'Наибольшая сумма {max_pair[0]} у числа {num_list[max_pair[1]]}'


if __name__ == '__main__':
    pass
    try:
        # print(num_1(int(input('Введите число: '))))
        # print(num_2(int(input('Введите число: '))))
        # print(num_3(int(input('Введите количество элементов: '))))
        # print(num_4(int(input('Введите число: '))))
        # print(num_5())
        # print(num_6(input('Введите числа через запятую: ')))
    except Exception as e:
        print(e)
