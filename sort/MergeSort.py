import math


class MergeSort():

    def merge(self, arr, front, end):

        mid = math.floor((front+end)/2)

        positive_infinity = math.inf

        # 將 front ~ mid 放至 leftSub[], 並在最後加入無限大元素
        leftSub = []
        leftCounter = front
        while leftCounter <= mid:
            leftSub.append(arr[leftCounter])
            leftCounter += 1

        leftSub.append(positive_infinity)

        # 將 mid+1 ~ end 放至 rightSub[], 並在最後加入無限大元素
        rightSub = []
        rightCounter = mid+1
        while rightCounter <= end:
            rightSub.append(arr[rightCounter])
            rightCounter += 1

        rightSub.append(positive_infinity)

        # loop i from front to end, execute merge
        i = front
        leftIndx = 0
        rightIndx = 0
        while i <= end:
            if leftSub[leftIndx] < rightSub[rightIndx]:
                arr[i] = leftSub[leftIndx]
                leftIndx += 1
            else:
                arr[i] = rightSub[rightIndx]
                rightIndx += 1

            i += 1

    def mergeSort(self, arr, front, end):

        if front < end:

            mid = math.floor((front+end)/2)

            self.mergeSort(arr, front, mid)

            self.mergeSort(arr, mid+1, end)

            self.merge(arr, front, end)


if __name__ == "__main__":
    arr = [3, 5, 7,  6, 2, 8]

    sort = MergeSort()

    sort.mergeSort(arr, 0, len(arr)-1)

    print(f'{arr}')
