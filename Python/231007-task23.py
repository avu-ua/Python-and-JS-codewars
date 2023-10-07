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

# ------------------------ Mariia ------------------------
def find_the_crossing(a, b, c, d):
    try:
        x = ((a[0]*b[1] - a[1]*b[0])*(c[0] - d[0]) - (a[0] - b[0])*(c[0]*d[1] - c[1]*d[0])) / ((a[0] - b[0])*(c[1] - d[1]) - (a[1] - b[1])*(c[0] - d[0]))
        y = ((a[0]*b[1] - a[1]*b[0])*(c[1] - d[1]) - (a[1] - b[1])*(c[0]*d[1] - c[1]*d[0])) / ((a[0] - b[0])*(c[1] - d[1]) - (a[1] - b[1])*(c[0] - d[0]))
    except: return None
    return (x,y)

# ------------------ Slava --------------------------
def find_the_crossing(a, b, c, d):
    z = ((a[0] - b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] - d[0]))
    if not z: return None
    x = ((a[0] * b[1] - a[1] * b[0]) * (c[0] - d[0]) - (a[0] - b[0]) * (c[0] * d[1] - c[1] * d[0])) / z
    y = ((a[0] * b[1] - a[1] * b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] * d[1] - c[1] * d[0])) / z
    return (x, y)
