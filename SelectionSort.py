def selectionSort(lst):
    for i in range(len(lst) - 1):
        currentMin = lst[i]
        currentMinIndex = i

        for j in range(i + 1, len(lst)):
            if currentMin > lst[j]:
                currentMin = lst[j]
                currentMinIndex = j

        if currentMinIndex != i:
            lst[currentMinIndex] = lst[i]
            lst[i] = currentMin

    return lst

s = input('Enter Five Numbers separated by space: ')
items = s.split()
lst = [eval(x) for x in items]
print(lst)
print(selectionSort(lst))