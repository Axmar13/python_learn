def array_diff(a, b):
    i = 0
    while i < len(a):
        if a[i] in b:
            a.remove(a[i])
            i = 0
        else:
            i += 1
    return a


print(array_diff([1,2,2], [2]))

'''
def array_diff(a, b):
    return [x for x in a if x not in b]
'''