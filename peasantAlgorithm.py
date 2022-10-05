def peasant(x, y):
    if x == 0:
        return x
    else:
        # x_component and y_component are being computed in both the recurrences
        x = x // 2
        y = y + y
        prod = peasant(x, y)
        # now if x is odd the only difference is our prod gets incremented by y
        if x % 2 != 0:
            prod = prod + y
        return prod


if __name__ == '__main__':
    print(peasant(24, 5))
