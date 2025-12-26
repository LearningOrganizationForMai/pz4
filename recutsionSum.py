def rec_summ(ar):
    s = 0
    for i in ar:
        if isinstance(i, ((int, float))):
            s += i
        else:
            s += rec_summ(i)
    return s

print(rec_summ([1, [2,3], [4, [5,6]], [-1, -5], 0]))
