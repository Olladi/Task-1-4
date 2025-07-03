import sys
import math

circle_file = sys.argv[1]
points_file = sys.argv[2]

with open(circle_file, 'r') as f:
    cx_cy = f.readline().split()
    cx = float(cx_cy[0])
    cy = float(cx_cy[1])
    radius = float(f.readline())

with open(points_file, 'r') as f:
    points = [line.strip().split() for line in f if line.strip()]

for point in points:
    x = float(point[0])
    y = float(point[1])
    dist = math.hypot(x - cx, y - cy)

    if abs(dist - radius) < 1e-9:
        print(0)
    elif dist < radius:
        print(1)
    else:
        print(2)