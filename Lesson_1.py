import random


def num_1(td_num: int) -> str:
    sm = 0
    mul = 1
    if 99 < td_num < 1000:
        for i in str(td_num):
            i = int(i)
            sm += i
            mul *= i
            res = f'Сумма - {sm}, произведенеие - {mul}'
    else:
        raise ValueError('Повторите ввод')
    return res


def num_2(a=5, b=6) -> str:
    bin_a = ''
    bin_b = ''
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    while b > 0:
        bin_b = str(b % 2) + bin_b
        b = b // 2
    # операции без учета случая разной разрядности двоичных чисел
    a_and_b_man = ''
    a_or_b_man = ''
    for i in range(len(bin_a)):
        a_and_b_man += '1' if bin_a[i] == '1' and bin_b[i] == '1' else '0'
        a_or_b_man += '1' if bin_a[i] == '1' or bin_b[i] == '1' else '0'
    a_and_b = int(bin_a, 2) & int(bin_b, 2)
    a_or_b = int(bin_a, 2) | int(bin_b, 2)
    a_ll = int(bin_a, 2) << 2
    a_rr = int(bin_a, 2) >> 2
    a_ll_man = bin_a[:]
    a_rr_man = bin_a[:]
    for _ in range(2):
        a_ll_man += '0'
        a_rr_man = '0' + a_rr_man
        a_rr_man = a_rr_man[:-1]
    return f'{bin_a} И {bin_b} = {a_and_b_man} (проверка - {bin(a_and_b)}), {bin_a} ИЛИ {bin_b} = {a_or_b_man} (проверка - {bin(a_or_b)}); {bin(a_ll)} = {a_ll_man}; {bin(a_rr)} = {a_rr_man}'


def num_3(coord: str) -> str:
    crd_lst = list(map(int, coord.split(',')))
    k = crd_lst[3] - crd_lst[1]
    b = crd_lst[2] - crd_lst[0]
    res = f'y = {k}*x + {b}'
    return res


def num_4() -> str:
    a = int(input('Полчить целое число не менее чем: '))
    b = int(input('Полчить целое число не более чем: '))
    res_1 = random.randint(a, b)
    c = int(input('Полчить вещественное число не менее чем: '))
    d = int(input('Полчить вещественное число не более чем: '))
    res_2 = random.uniform(c, d)
    e = ord(input('Полчить символ в диапазоне от: '))
    f = ord(input('Полчить символ в диапазоне до: '))
    res_3 = chr(random.randint(e, f))
    res = f'{res_1}, {res_2}, {res_3}'
    return res


def num_5(lets: str) -> list:
    lets_ord_list = list(map(ord, lets.split(',')))
    lets_ord_list.append(lets_ord_list[0] - lets_ord_list[1])
    if lets_ord_list[2] < 0:
        lets_ord_list[2] = -lets_ord_list[2]
    return lets_ord_list


def num_6(let_num: int) -> str:
    if 1 <= let_num <= 26:
        res = chr(96 + let_num)
    else:
        raise ValueError('Повторите ввод')
    return res


def num_7() -> str:
    a = int(input('Введите длину стороны А: '))
    b = int(input('Введите длину стороны B: '))
    c = int(input('Введите длину стороны C: '))
    if a * b * c:
        if a == b == c:
            res = 'Равносторонний'
        elif a != b != c != a:
            res = 'Разносторонний'
        else:
            res = 'Равнобедренный'
    else:
        res = 'Треугольник построить невозможно'
    return res


def num_8(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def num_9() -> str:
    a = int(input('Введите число 1: '))
    b = int(input('Введите число 2: '))
    c = int(input('Введите число 3: '))
    if a < b < c or c < b < a:
        return b
    elif a < c < b or b < c < a:
        return c
    elif b < a < c or c < a < b:
        return a
    else:
        raise ValueError('Повторите ввод')


if __name__ == '__main__':
    pass
    try:
        # print(num_1(int(input('1. Введите 3-значное число: '))))
        # print(num_2())
        # print(num_3(input('Введите х1,у1,х2,у2 подряд через запятую: ')))
        # print(num_4())
        # print(num_5(input('Введите две буквы через запятую без пробела: ')))
        # print(num_6(int(input('Введите номер буквы: '))))
        # print(num_7())
        # print(num_8(int(input('Введите год на проверку високосности: '))))
        # print(num_9())
    except Exception as e:
        print(e)
