def num_1(input_n: int) -> str:
    even = 0
    n = 0
    while input_n > 0:
        num = input_n % 10
        if num % 2 == 0:
            even += 1
        n += 1
        input_n //= 10
    res = f'Четных - {even}, нечетных - {n - even}'
    return res


def num_2(input_n: int) -> int:
    res = 0
    while input_n > 0:
        num = input_n % 10
        input_n //= 10
        res = res * 10 + num
    return res


def num_3(input_n: int) -> float:
    res = 0
    f = 1
    for _ in range(input_n):
        res += f
        f /= -2
    return res


def num_3_rec(n: int) -> float:
    if n == 0:
        return 0
    else:
        return num_3_rec(n - 1) + (-0.5) ** (n - 1)


def num_4(input_n: int) -> bool:
    def helper(n: int) -> int:
        if n == 0:
            return 0
        else:
            return helper(n - 1) + n

    res_2 = input_n * (input_n + 1) / 2
    check = True if helper(input_n) == res_2 else False
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
    def helper(n: int) -> int:
        if n == 0:
            return 0
        else:
            m = n % 10
            return helper(n//10) + m
    num_list = list(map(int, nums.split(',')))
    smax = helper(num_list[0])
    for i in range(len(num_list)):
        if helper(num_list[i]) > smax:
            smax = helper(num_list[i])
            imax = i
    return f'Наибольшая сумма {smax} у числа {num_list[imax]}'


class Solution:
    def reverseString(self, s: list[str]):
        if not s:
            return []
        else:
            n = s[0]
            s = self.reverseString(s[1:])
            s.append(n)
            return s



if __name__ == '__main__':
    pass
    try:
        # print(num_1(int(input('Введите число: '))))
        # print(num_2(int(input('Введите число: '))))
        # print(num_3(int(input('Введите количество элементов: '))))
        # print(num_3_rec(int(input('Введите количество элементов: '))))
        # print(num_4(int(input('Введите число: '))))
        # print(num_5())
        print(num_6(input('Введите числа через запятую: ')))
        #
        # Задание на рекурсию - так и не получилось решить на Литкод, хотя в pycharm работает.
        # Там выдаёт output такой же как input
        s = ["h", "e", "l", "l", "o"]
        s_2 = ["H", "a", "n", "n", "a", "h"]
        sol = Solution()
        print(sol.reverseString(s))
        print(sol.reverseString(s_2))
    except Exception as e:
        print(e)
