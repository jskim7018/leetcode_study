def get_value(n, x, y):
    value = 0
    while n > 0:
        half = 1 << (n - 1)
        quadrant_size = 1 << (2 * (n - 1))
        if x <= half and y <= half:
            quadrant = 0
        elif x > half and y > half:
            quadrant = 1
            x -= half
            y -= half
        elif x > half:
            quadrant = 2
            x -= half
        else:
            quadrant = 3
            y -= half
        value += quadrant * quadrant_size
        n -= 1
    return value + 1

def get_coordinates(n, d):
    x = y = 1
    d -= 1
    while n > 0:
        half = 1 << (n - 1)
        quadrant_size = 1 << (2 * (n - 1))
        quadrant = d // quadrant_size
        d %= quadrant_size
        if quadrant == 1:
            x += half
            y += half
        elif quadrant == 2:
            x += half
        elif quadrant == 3:
            y += half
        n -= 1
    return x, y

t = int(input())
for _ in range(t):
    n = int(input())
    q = int(input())
    for _ in range(q):
        line = input().strip()
        if line.startswith("->"):
            _, x, y = line.split()
            print(get_value(n, int(x), int(y)))
        elif line.startswith("<-"):
            _, d = line.split()
            x, y = get_coordinates(n, int(d))
            print(x, y)

