

def binary_search_recursive(lst, target, left, right, count=0):
    if left > right:
        print(count)
        return None

    mid = (left + right) // 2
    count += 1

    if lst[mid] == target:
        return (index, count)
        pass  # return index and count
    elif lst[mid] < target:
        count += 1
        return binary_search_recursive(lst[mid],target,right)
    else:
        return binary_search_recursive(lst[mid],target,right)

lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
index, comparisons = binary_search_recursive(lst, 13, 0, len(lst) - 1)
print(f"Found at index {index} in {comparisons} comparisons.")

index, comparisons = binary_search_recursive(lst, 4, 0, len(lst) - 1)
print(f"Not found. Comparisons made: {comparisons}.")