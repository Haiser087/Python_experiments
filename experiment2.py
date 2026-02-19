def findMinMax(arr):
    arr = [1, 2, 3, 4, 5]
    min = arr[0]
    max = arr[0]
    for i in arr:
        if i < min:
            min = i
        elif i > max:
            max = i

    print("Minimum element is:", min)
    print("Maximum element is:", max)