def dynamicex(s, t):
    def recurse(m, n):
        if m == 0:
            result = n
        elif n == 0:
            result = m
        elif s[m-1] == t[n-1]:
            result = recurse(m-1, n-1)
        else:
            subcost = 1 + recurse(m-1, n-1)
            inscost = 1 + recurse(m, n-1)
            delcost = 1 + recurse(m-1, n)
            result = min(subcost, inscost, delcost)
        return result
    return recurse(len(s), len(t))

print(dynamicex("ca!", "ba!"))
