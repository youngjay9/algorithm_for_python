
"""
https://leetcode-cn.com/problems/generate-parentheses/
"""


class CreateParenthesis:

    def generateParenthesis(self, n):
        self.list = []
        self.n = n
        self._gen(0, 0, "")

        return self.list

    def _gen(self, left, right, result):

        if left == self.n and right == self.n:
            self.list.append(result)
            return

        if left < self.n:
            self._gen(left+1, right, result+"(")

        if left > right and right < self.n:
            self._gen(left, right+1, result+")")


if __name__ == "__main__":
    createParenthesis = CreateParenthesis()
    createParenthesis.generateParenthesis(3)
