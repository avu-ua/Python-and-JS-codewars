# https://www.codewars.com/kata/63a5b74a9803f2105fa838f1

# ------------------------ Olesia ------------------------
def find_the_crossing(a, b, c, d):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    x4, y4 = d

    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if denominator == 0:
        return None

    x_crossing = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) /denominator
    y_crossing = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) /denominator

    return x_crossing, y_crossing
