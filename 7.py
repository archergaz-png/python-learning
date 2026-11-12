def search(haystack, needle): 
    for i, item in enumerate(haystack):
        if item == needle:
            return i
    return-1

f = [4,5,6,7]
idx = search(f,7) # 4 iter
idx = search(f,4) # 4 iter
print(idx)

def bin_search (haystack, needle):
    low, high = 0, len(needle)
    
    while low < high:
        mid = (high + low)//2
        if haystack[mid] == needle:
            return idx

        if haystack[mid] > needle:
            high = mid

    if haystack[mid] < needle:
        low = mid+1

        print (haystack[idx])
        idx += 1

hay = [1,2,3,4,5]
needle = 4
""""""
# 

Res = bin_search(hay, needle)
print(hay)
print(needle)
print()

i =()
high = ()






hay = [1,5,89,345,9,35]
sorted(hay)
# sorting massive





