class Solution(object):

    def __init__(self):
        # 將運算結果暫存
        self.resolvedList = None

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        self.resolvedList = {}

        if n >= 0:
            return self.pow(x, n)
        elif n < 0:
            return 1 / self.pow(x, -n)

    def pow(self, x, n):
        # 設定 recursive 的終止條件
        if n == 0:
            return 1

        if n == 1:
            return x

        # 有在之前的計算結果,直接取值,減少呼叫 stack 的次數已減少記憶體使用
        if n in self.resolvedList.keys():
            return self.resolvedList[n]

        # even
        if n % 2 == 0:
            tmp = self.pow(x, n/2)
            res = tmp * tmp
            self.resolvedList[n/2] = res
            return res

        # odd
        tmp = self.pow(x, (n-1)/2)
        res = x * tmp * tmp
        self.resolvedList[(n-1)/2] = res
        return res


if __name__ == "__main__":
    solution = Solution()

    print(f'{solution.myPow(2, 10)}')

    print(f'{solution.myPow(2, 10)}')
