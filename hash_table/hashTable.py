class HashTable:

    def __init__(self, size):
        self.size = size
        """ 
            hashTable 是一個 dictionary 資料結構, key 放 indx, value 放 list 
            {
                0: [{'jay': 36}, {'james':35}, {'wade': 37}],
                1: [{'wang': 40}, {'jenny': 30}, {'summer': 35}],
            }
        """
        self.data = {}

    """ 定義自行 hash 的方式將 key 轉成 index """

    def myHash(self, key):
        hash = 0

        for i in range(len(key)):
            # ord(key[i]) 是取得字元對應的 ASCII 數字
            hash = (hash + ord(key[i]) * i) % self.size

        return hash

    """ 將 key hash 後的 indx 值放入 hashTable """

    def put(self, key, value):
        indx = self.myHash(key)

        # ditionary 的 key 是 indx, value 是一個 list
        if indx not in self.data.keys():
            self.data[indx] = []

        # 把 value append 到 list
        self.data[indx].append({key: value})

        return self.data

    """ 將 key hash 後的 indx 值，至 hashTable 找對應的 value """

    def get(self, key):
        indx = self.myHash(key)

        # 從 hashTable 對應的 indx 取出 list
        currentBucket = self.data[indx]

        # 從 list
        if currentBucket:
            for item in currentBucket:
                if item[key] is not None:
                    return item[key]
        return None

    """ 回傳 hashTable value 中的 keys """

    def keys(self):

        result = []

        for item in self.data.values():  # dictionary 的 value 是 list
            for l in item:  # list 裡面是 dictionary
                for k in l.keys():
                    result.append(k)

        return result
