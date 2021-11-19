"""
    Recursive 的 Big O 為： 2^n
    消耗太多時間及記億體, 需評估狀況後用 dynamic programming 替代它
"""
class Recursive:
    def __init__(self) -> None:
        pass


    def factorial(self,n):
        if n == 0:
            return 1

        return n * self.factorial(n-1)

    """ 第 n 項 = (n-1) + (n-2)"""
    def fibonacci(self, n):
        # n 為 0 or 1, 回傳 n
        if n < 2:
            return n

        return self.fibonacci(n-1) + self.fibonacci(n-2)

    
    
    def reverse(self, str, indx):
        print(f'{str[indx]}')
        if indx == 0:
            return

        self.reverse(str, indx - 1)    
    
    '''
     利用 recursive reverse 一個字串
    '''
    def reverseString(self, str):
        indx = len(str) - 1
        self.reverse(str, indx)

        

if __name__ == "__main__":
    
    recursive = Recursive()

    # print(f'{recursive.factorial(5)}')

    # print(f'{recursive.fibonacci(40)}')

    recursive.reverseString('Jay')