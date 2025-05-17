from typing import List


def binary_search(arr: List[int], target: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)

        if arr[mid] > target:
            high = mid - 1

        elif arr[mid] < target:
            low = mid + 1

        else:
            return mid

    return -1


def main() -> None:
    arr = [1, 3, 5, 8, 13, 21, 55, 89, 144, 233]
    target = 8
    result = binary_search(arr, target)

    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in list")


if __name__ == "__main__":
    main()
