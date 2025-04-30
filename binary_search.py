def binary_search(arr: list, target: int, low: int, high: int) -> int:
    while low <= high:
        # find mid point
        mid = low + (high - low) // 2

        # if we found the index
        if arr[mid] == target:
            return mid

        # if mid point is less than the number we are too low
        elif arr[mid] < target:
            low = mid + 1

        # if mid point is more than number we are too high
        else:
            high = mid - 1

    # low > high, meaning item not contained
    return -1


def main() -> None:
    arr = [1, 3, 5, 8, 13, 21]
    target = 8
    low = 0
    high = len(arr) - 1
    result = binary_search(arr, target, low, high)

    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in list")


if __name__ == "__main__":
    main()
