known = {}


def ack(m, n):
    """Evaluates the Ackermann function."""

    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)

    if (m, n) in known:
        return known[m, n]
    else:
        known[m, n] = ack(m - 1, ack(m, n - 1))
        return known[m, n]


print(ack(3, 4))

for item in known:
    print(item, known[item])
