from inspect import stack
from unicodedata import name


class Solution:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_table = {"(": ")", "[": "]", "{": "}"}

        stack = []

        for c in s:
            print(f'{c}')
            # 左括號押入 stack
            if c in p_table.keys():
                stack.append(c)
            else:
                # 右括號, 取出 stack popUp 的左括號
                pop_c = stack.pop()
                # 檢查 popUp 的左括號對應的右括號是否相同
                if c != p_table[pop_c]:
                    return False
        # 如果 stack 不為空, 代表 s 為不合法字串
        return not stack


if __name__ == "__main__":

    solution = Solution()

    is_valid = solution.isValid("()[]{")

    print(f'is_valid: {is_valid}')
