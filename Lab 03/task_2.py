def maxValue(arr):
    if len(arr) > 1:
        l = len(arr)
        mid = l // 2
        left = maxValue(arr[:mid])
        right = maxValue(arr[mid:])
        if left > right:
            return left
        else:
            return right
    return arr[0]

with open('input2.txt', 'r') as f:
    N, arr = f.readlines()
    N, arr = int(N), list(map(int, arr.split()))

with open('output2.txt', 'w') as f:
    f.write(str(maxValue(arr)))

#The time complexity of this code will be O(nlogn).