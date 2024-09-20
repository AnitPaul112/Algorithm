def maxValue(arr):
    if len(arr) > 1:
        l = len(arr)
        mid = l // 2
        left = arr[:mid]
        right = arr[mid:]
        l_max = maxValue(left)
        r_max = maxValue(right)
        x = [int(i)*-1 for i in right]
        max_val = max(left) + max(x)**2 + max(right)
        max_sum = max(left) + max(right)
        max_val = max_sum + max_sum**2
        return max(l_max, r_max, max_val)
    return max(arr)  # O(n)


with open('input4.txt', 'r') as f:
    N, arr = f.readlines()
    N, arr = int(N), list(map(int, arr.split()))

with open ('output4.txt', 'w') as f:
    f.write(str(maxValue(arr)))