import time


class QuickSortOptmized():

    ''' insertion sort'''

    def insertion_sort(self, arr, low, n):

        for i in range(low + 1, n + 1):

            val = arr[i]

            j = i

            while j > low and arr[j-1] > val:

                arr[j] = arr[j-1]

                j -= 1

            arr[j] = val

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

    def optmized_quick_sort(self, arr, front, end):
        while front < end:
            if (end - front) + 1 < 10:
                self.insertion_sort(arr, front, end)
                break
            else:
                # 先對 arr 進行 partition, 並回傳 partition 後 pivot 數字的 index
                partition_indx = self.partition(arr, front, end)

                # 左半部 subArray size 較小, 有機會先進行 insertion sort
                if partition_indx - end < end - partition_indx:
                    self.optmized_quick_sort(arr, front, partition_indx - 1)
                    # 指定下一輪排序從右半部 subArray 開始
                    front = partition_indx + 1
                # 右半部 subArray size 較小, 有機會先進行 insertion sort
                else:
                    self.optmized_quick_sort(arr, partition_indx+1, end)
                    # 指定下一輪排序從左半部 subArray 開始
                    end = partition_indx - 1


if __name__ == "__main__":
    sort = QuickSortOptmized()
    arr = [24, 97, 40, 67, 88, 85, 15,

           66, 53, 44, 26, 48, 16, 52,

           45, 23, 90, 18, 49, 80]

    begin1 = time.time() * 1000000000
    sort.optmized_quick_sort(arr, 0, len(arr)-1)
    end1 = time.time() * 1000000000

    # print(f'{arr}')

    print(f'optmized_quick_sort: {end1-begin1} ns')

    begin2 = time.time() * 1000000000
    sort.quick_sort(arr, 0, len(arr)-1)
    end2 = time.time() * 1000000000

    print(f'quick_sort: {end2-begin2} ns')
