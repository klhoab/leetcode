def powerset(s):
    x = len(s)
    ans = []
    for i in range(1 << x):
        t= sorted([s[j] for j in range(x) if (i & (1 << j))])
        if t not in ans:
            ans= ans + [t]
    return ans


print(powerset([1,2,2]))
