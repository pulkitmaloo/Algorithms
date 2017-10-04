# Top down
price = [1, 5, 8, 9, 10, 17, 17, 20]
val = [0]+[-1]*len(price)
def top_down_cutRod(n=len(price), r=val, p=price):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        return 0
    else:
        val[n] = max([p[i-1] + top_down_cutRod(n-i, r, p) for i in range(1, n+1)])
        return val[n]

top_down_cutRod()
print val

# Bottom up
price = [1, 5, 8, 9, 10, 17, 17, 20]
def cutRod(n=len(price), p=price):
    val = [0]*(n+1)
    val[0] = 0
    for i in range(1, n+1):
        val[i] = max([p[j-1]+val[i-j] for j in range(1, i+1)])
    return val[n]

print cutRod()