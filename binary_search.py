from typing import List


def binary_search(arr: List[int], target: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)

        # if number too high, search left half
        if arr[mid] > target:
            high = mid - 1

        # if number too low, search right half
        elif arr[mid] < target:
            low = mid + 1

        else:
            return mid

    return -1


def recursive_binary_search(arr: List[int], target: int, low: int, high: int) -> int:
    if low > high:
        return -1

    mid = low + ((high - low) // 2)

    # if number too high, search left half
    if arr[mid] > target:
        return recursive_binary_search(arr, target, low, mid - 1)

    # if number too low, search right half
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high)

    else:
        return mid


def main() -> None:
    arr = [1, 3, 5, 8, 13, 21, 55, 89, 144, 233]
    target = 8
    result = binary_search(arr, target)
    result2 = recursive_binary_search(arr, target, 0, len(arr) - 1)

    print("Iterative")
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in list")

    print("Recursive")
    if result2 != -1:
        print(f"Element is present at index {result2}")
    else:
        print("Element is not present in list")


if __name__ == "__main__":
    main()
