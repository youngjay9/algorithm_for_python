from unittest import result


class Solution():

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        items1 = {}

        items2 = {}

        result = True

        # loop 字串 s, 將每個字母的數量放進 items1
        for c in s:
            if c not in items1.keys():
                items1[c] = 1
            else:
                items1[c] = items1[c]+1

        for c in t:
            if c not in items2.keys():
                items2[c] = 1
            else:
                items2[c] = items2[c]+1

        print(f'items1 len: {len(items1)}')

        # 比較 items1 與 items2 的字母與其數量是否都相同
        return items1 == items2


if __name__ == "__main__":

    solution = Solution()

    s = "anagram"

    t = "nagaram"

    result = solution.isAnagram(s, t)

    print(f'result: {result}')
