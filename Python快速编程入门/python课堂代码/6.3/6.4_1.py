def move(x, y, step):
    nx = x + step
    ny = y - step
    return nx, ny


res = move(100, 100, 60)
print(res)
