import time


class QuickSort():
    '''
        指定 pivot = arr[end], 並回傳 pivot 的 index
    '''

    def partition(self, arr, front, end):
        pivot = arr[end]
        i = front-1
        j = front

        while j < end:
            if arr[j] < pivot:
                i += 1
                # swap arr[i] and arr[j]
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp

            j += 1

        i += 1
        # swap arr[i] and arr[end]
        tmp = arr[i]
        arr[i] = arr[end]
        arr[end] = tmp

        return i

    def quick_sort(self, arr, front, end):
        if front < end:
            # 先對 arr 進行 partition, 並回傳 partition 後 pivot 數字的 index
            partition_indx = self.partition(arr, front, end)

            # 對 partition 左方進行 quick sort
            self.quick_sort(arr, front, partition_indx-1)

            # 對 partition 右方進行 quick sort
            self.quick_sort(arr, partition_indx+1, end)


if __name__ == "__main__":
    quick_sort = QuickSort()

    # arr = [9, 4, 1, 6, 7, 3, 8, 2, 5]

    arr = [24, 97, 40, 67, 88, 85, 15,

           66, 53, 44, 26, 48, 16, 52,

           45, 23, 90, 18, 49, 80]

    begin = time.time() * 1000000000

    quick_sort.quick_sort(arr, 0, len(arr)-1)

    end = time.time() * 1000000000

    print(f'{arr}')

    print(f'{end-begin} ns')
