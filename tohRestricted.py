def tohRestricted(n, a, b):
    # a=0, b=1, c=2
    if n > 0:
        if a == 0 or b == 0:
        #if (a == 0 and b == 1) or (a == 2 and b == 0) or (a == 1 and b == 0) or (a == 0 and b == 2):
            if n == 1:
                print('Move disk', n, 'from', a, 'to', b)
            tohRestricted(n - 1, a, b)
        elif a != 0 and b != 0 and a != b:
        # elif (a == 1 and b == 2) or (a == 2 and b == 1):
            if n == 1:
                print('Move disk', n, 'from', a, 'to', 0)
                print('Move disk', n, 'from', 0, 'to', b)
            tohRestricted(n - 1, a, b)

if __name__ == '__main__':
    tohRestricted(3, 0, 2)
