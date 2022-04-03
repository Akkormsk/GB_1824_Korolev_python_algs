import random


def main():
    m = random.randint(2, 4)
    l = 2 * m + 1
    arr = []
    while len(arr) < l:
        num = random.randint(1, l)
        if num not in arr:
            arr.append(num)
    print(arr)

    def search(array, index):
        if len(array) == 1:
            return array[0]
        pivot = array[random.randint(0, len(array) - 1)]
        left = [num for num in array if num <= pivot]
        right = [num for num in array if num > pivot]
        if len(left) > index:
            return search(left, index)
        else:
            return search(right, index-len(left))

    return search(arr, m)


if __name__ == '__main__':
    print(main())
