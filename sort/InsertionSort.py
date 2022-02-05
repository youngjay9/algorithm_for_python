class InsertionSort():
    def insertion_sort(self, arr):
        i = 1

        for i in range(1, len(arr)):
            insert_num = arr[i]
            count = i-1

            while count >= 0 and arr[count] > insert_num:
                # 執行 shift right
                arr[count+1] = arr[count]
                count -= 1

            arr[count+1] = insert_num


if __name__ == "__main__":

    arr = [5, 3, 1, 2, 6, 4]

    print(f'before sort: {arr}')

    sort = InsertionSort()

    sort.insertion_sort(arr)

    print(f'after sort: {arr}')
