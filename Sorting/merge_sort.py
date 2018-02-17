def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high)/2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
    return arr

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    L = [0]*n1
    R = [0]*n2
    for i in range(0, int(n1)):
        L[i] = arr[low + i]
    for j in range(0, int(n2)):
        R[j] = arr[mid + 1 + j]
    i = 0
    j = 0
    k = low
    while i < n1 and j < n2:
        if R[j] >= L[i]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        k += 1
        i += 1
    while j < n2:
        arr[k] = R[j]
        k += 1
        j += 1