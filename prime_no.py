print([x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
