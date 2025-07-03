def get_circular_path(n, m):
    path = []
    i = 1
    while True:
        path.append(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    return path
