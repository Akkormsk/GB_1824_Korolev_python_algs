import random

"""
Сначала решил разобраться с задачей, разобранной на вебинаре, так как на литкоде представлен только кусок кода
"""


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_list_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

    def list_length(self):
        count = 0
        curr = self.head
        while curr:
            curr = curr.next
            count += 1
        return count

    def output_list(self):
        curr = self.head
        while curr:
            print(curr.data, end='')
            curr = curr.next

    def rev_list(self):
        curr = self.head
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev


"""
ДЗ
"""


def num_1() -> str:
    res = 'В диапазоне от 2 до 99:' + '\n'
    list_k = [0] * 8
    for i in range(2, 10):
        list_k[i - 2] = 99 // i
        res += f'Кратно {i} - {list_k[i - 2]} чисел' + '\n'
    return res


def num_2() -> str:
    leng = int(input('Ввудите длину массива: '))
    m = []
    min_i = 0
    max_i = 0
    for i in range(leng):
        m.append(random.randint(1, 100))
        if m[i] > m[max_i]:
            max_i = i
        if m[i] < m[min_i]:
            min_i = i
    res = f'arr = {m}, max_i = {m[max_i]}, min_i = {m[min_i]}'
    m[max_i], m[min_i] = m[min_i], m[max_i]
    res += f', reversed arr = {m}'
    return res


def num_3() -> int:
    leng = int(input('Ввудите длину массива: '))
    m = []
    min_i = 0
    max_i = 0
    for i in range(leng):
        m.append(random.randint(1, 100))
        if m[i] > m[max_i]:
            max_i = i
        if m[i] < m[min_i]:
            min_i = i
    print(m, 'min = ', m[min_i], 'max = ', m[max_i])
    summ = 0
    if min_i > max_i:
        min_i, max_i = max_i, min_i
    for i in range(min_i + 1, max_i):
        summ += m[i]
    return summ


def num_4():
    leng = int(input('Ввудите длину массива: '))
    m = []
    min_i_1 = 0
    min_i_2 = 0
    for i in range(leng):
        m.append(random.randint(1, 100))
        if m[i] < m[min_i_2]:
            min_i_2 = i
        if m[i] <= m[min_i_1]:
            min_i_2 = min_i_1
            min_i_1 = i
    return f'arr = {m}, min_1 = {m[min_i_1]}, min_2 = {m[min_i_2]}'


if __name__ == '__main__':
    # track = SLL()
    # a = 'a'
    # b = 'b'
    # c = 'c'
    # d = 'd'
    # for i in [a, b, c, d]:
    #     track.add_list_item(i)
    # print(f'Track length: {track.list_length()}')
    # track.output_list()
    # track.rev_list()
    # print('\nReversed track:')
    # track.output_list()

    print(num_1())
    # print(num_2())
    # print(num_3())
    # print(num_4())
