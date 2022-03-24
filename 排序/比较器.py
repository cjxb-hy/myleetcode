from functools import cmp_to_key


def comp(x, y):
    if x[0] != y[0]:
        return x[0] - y[0]
    return x[1] - y[1]


if __name__ == '__main__':
    alist = [[3, 6], [8, 0], [2, 1], [5, 7], [5, 2]]
    print(sorted(alist, key=cmp_to_key(comp)))
