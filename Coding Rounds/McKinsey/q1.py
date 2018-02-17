def bs_lower(scores, x):
    low = 0
    high = len(scores) - 1
    while (low <= high):
        mid = int((low + high)/2)
        if scores[mid] >= x:
            high = mid - 1
        else:
            low = mid + 1
    return low

def bs_upper(scores, x):
    low = 0
    high = len(scores) - 1
    while (low <= high):
        mid = int((low + high)/2)
        if scores[mid] <= x:
            low = mid + 1
        else:
            high = mid - 1
    return high
    
def count(scores, l, r):
    return bs_upper(scores, r) - bs_lower(scores, l) + 1

def jobOffers(scores, lowerLimits, upperLimits):
    scores.sort()
    res = []
    for (l, u) in zip(lowerLimits, upperLimits):
        res.append(count(scores, l, u))
    return res

if __name__ == '__main__':
	res = jobOffers([1,3,4,5,6,7,8],[2],[5])
	print(res)
