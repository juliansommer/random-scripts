def binary_search(list: list, target: int, low: int, high: int) -> int:
    if low > high:
        return -1
    mid = (low + high) // 2
    if list[mid] == target:
        return mid
    elif list[mid] > target:
        return binary_search(list, target, low, mid - 1)
    else:
        return binary_search(list, target, mid + 1, high)


def main() -> None:
    list = [1, 3, 5, 8, 13, 21]
    target = 8

    result = binary_search(list, target, 0, len(list) - 1)

    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in list")


if __name__ == "__main__":
    main()
