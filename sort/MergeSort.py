import math

class MergeSort():
    
    def __init__(self, arr):
        self.arr = arr
    
    def merge(self, front, end):

        mid = math.floor((front+end)/2)

        positive_infinity = math.inf

        # 將 front ~ mid 放至 leftSub[], 並在最後加入無限大元素
        leftSub = []
        leftIndx = 0
        leftCounter = 0
        while leftCounter <= mid:
            leftSub.append(self.arr[leftCounter])
            leftCounter +=1

        leftSub.append(positive_infinity)
        
        # 將 front ~ mid+1 放至 leftSub[], 並在最後加入無限大元素
        rightSub = []
        rightIndx = 0
        rightCounter = 0
        while rightCounter <= end:
            rightSub.append(self.arr[rightCounter])
            rightCounter +=1

        rightSub.append(positive_infinity)

        # loop i from front to end, execute merge
        i = front
        while i <= end:
            if leftSub[leftIndx] < rightSub[rightIndx]:
                self.arr[i] = leftSub[leftIndx]
                leftIndx +=1
            else:
                self.arr[i] = rightSub[rightIndx]
                rightIndx+=1

            i+=1

    def mergeSort(self, front, end):
        
        if len(self.arr) == 1:
            return self.arr
        
        mid = math.floor((front+end)/2)
        self.mergeSort(front, mid)
        self.mergeSort(mid+1, end)
        self.merge(front, end)
         




if __name__ == "__main__":
    arr = [3, 5,7, 6,2,8]
    
    sort = MergeSort()
    
    

