import math


class BinarySearch(object):

    def bserach(self, arr, value):
        low = 0
        high = len(arr) - 1

        # 注意退出循環的條件是 low<= high, 不是 low < high
        while low <= high:
            # 避免記憶體溢位,使用下列寫法
            mid = math.floor((low+high)/2)

            if arr[mid] == value:
                return mid

            elif arr[mid] < value:
                low = mid+1

            else:
                high = mid-1

        return -1


if __name__ == "__main__":
    b = BinarySearch()

    arr = [3, 4, 6, 7, 10]

    indx = b.bserach(arr, 7)

    print(f'indx: {indx}')
