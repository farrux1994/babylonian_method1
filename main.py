def main(S, d):
    a = (S-d*d)/(2*d)
    b = a+d
    x = b-(a*a)/(2*b)

    return x

k = main(16, 4)
print(k)
