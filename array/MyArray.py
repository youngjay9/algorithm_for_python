# -*- coding: utf-8 -*-
class MyArray:
    '''construnctor 初始化 length = 0 與 data 為空物件'''

    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    '''新增元素到最後一個位置'''

    def push(self, item):
        self.data[self.length] = item
        self.length = self.length + 1
        return self.data

    '''pop out 最後一個元素'''

    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length = self.length - 1
        return lastItem

    '''指定 index 刪除元素'''

    def deleteAtIndex(self, index):
        item = self.data[index]
        self.shiftItem(index)
        return item

    def shiftItem(self, index):
        # 從指定的 index 後的元素往前移一格
        while index < len(self.data) - 1:
            self.data[index] = self.data[index+1]
            index = index + 1

        # 往左 shift 一格後，需刪除最後一個元素
        del self.data[self.length - 1]

        # array 長度減一
        self.length = self.length - 1


myArray = MyArray()

print(myArray.push('hi'))
print(myArray.push('you'))
print(myArray.push('are'))
print(myArray.push('a'))
print(myArray.push('pig'))


print(myArray.shiftItem(2))

print(myArray.data)
