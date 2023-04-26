def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i + 1]


def distance_between_points(list_pst):
    for a, b in pairwise(list_pst):
        yield ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


def sum_distance(list_pst):
    sum_ = 0
    for i in distance_between_points(list_pst):
        sum_ += i
    return sum_


if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]
    print(sum_distance(pts))
