def bubble_sort(haystack):
    high = len(haystack)

    for i in range(high - 1):

        print(f"ITERATION #{i}")
        print (haystack)

    for j in range (high - i - 1):
       
        if haystack[j] > haystack[j+1]:
            tmp = haystack[j]
            haystack[j] = haystack[j+1]
            haystack[j+1] = tmp
            print (f"\tITERATION #{j}")
    
hay = [100, 90, 45, 50, 40, 30, 20]
print ("Было ", hay)
bubble_sort(hay)
print ("Стало ", hay)

