def max_dot_product(a, b):
    res = 0
    while a:
        j=max(a)
        k=max(b)
        res+=j*k
        a.remove(j)
        b.remove(k)
    return res
print(max_dot_product([23],[39]))