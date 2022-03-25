def get_left(i):
    return 2 * i + 1


def get_right(i):
    return 2 * i + 2


def get_parrent(i):
    return (i - 1) // 2


class Heap:
    def __init__(self, n):
        self.array = []
        for i in range(n):
            self.array.append([i, 0])

    def swap(self, ind_1, ind_2):
        self.array[ind_1], self.array[ind_2] = self.array[ind_2], self.array[ind_1]

    def sift_down(self, i):
        while i <= n // 2 - 1:
            left_ch_i = get_left(i)
            right_ch_i = get_right(i)
            min_i = i
            if left_ch_i < n and ((self.array[left_ch_i][1] < self.array[min_i][1]) or
                                   (self.array[left_ch_i][1] == self.array[min_i][1] and
                                    self.array[left_ch_i][0] < self.array[min_i][0])):
                min_i = left_ch_i
            if right_ch_i < n and ((self.array[right_ch_i][1] < self.array[min_i][1]) or
                                   (self.array[right_ch_i][1] == self.array[min_i][1] and
                                    self.array[right_ch_i][0] < self.array[min_i][0])):
                min_i = right_ch_i
            if min_i != i:
                self.swap(i, min_i)
                i = min_i
            else:
                break

    def sift_up(self, i):
        while i > 0 and self.array[get_parrent(i)] > self.array[i]:
            self.swap(get_parrent(i), i)
            i = get_parrent(i)

    def add(self, val):
        self.array.append(int(val))
        self.sift_up(len(self.array) - 1)

    def extract_min(self):
        min = self.array[0]
        self.swap(0, len(self.array) - 1)
        self.array.pop()
        self.sift_down(0)
        return min

    def get_min(self):
        return self.array[0]

    def change_priority(self, i, new_time):
        self.array[i][1] += new_time
        self.sift_down(i)

    def build_heap(self, n):
        for i in range(n):
            self.sift_down(i)


def main():
    heap = Heap(n)
    result = []
    # heap.build_heap(n)
    for i in range(m):
        # result.append(heap.get_min()[:])
        print(' '.join(map(str, heap.get_min())))
        heap.change_priority(0, mass[i])
    # print(result)


if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    mass = list(map(int, input().split(' ')))
    main()
