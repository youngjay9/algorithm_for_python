def merge(arr1, arr2):
    lIndx = 0  # arr1 用的 index
    lLength = len(arr1)

    rIndx = 0  # arr2 用的 index
    rLength = len(arr2)

    indx = 0  # merged array 用的 index
    result = []  # merge 後的 array

    # 比較 arr1 與 arr2
    while lIndx < lLength and rIndx < rLength:
        if arr1[lIndx] < arr2[rIndx]:
            result.append(arr1[lIndx])
            lIndx = lIndx + 1
        else:
            result.append(arr2[rIndx])
            rIndx = rIndx + 1

        indx = indx + 1

    # 將 arr1 or arr2 未跑完的 element 加入 arr
    while lIndx < lLength:
        result.append(arr1[lIndx])
        lIndx = lIndx + 1
        indx = indx + 1

    while rIndx < rLength:
        result.append(arr2[rIndx])
        rIndx = rIndx + 1
        indx = indx + 1

    return result


arr1 = [0, 3, 4, 31]

arr2 = [4, 6, 30]

r = merge(arr1, arr2)

print(f"two merged array: {r}")
