list = [1, 3, 5, 8, 13, 21]
target = 5

def binary_search(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print(binary_search(list, target))

