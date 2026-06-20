class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # inputs: list of ints (numbers to be assessed), k (number of top counts to return)
        # # outputs: list of k most freq elements

        # # let's use a hashmap to keep track of numbers
        # hmap = {}

        # for i in nums:
        #     if i in hmap.keys():
        #         hmap[i] += 1
        #     else:
        #         hmap[i] = 1
            
        # retlist = []
        # for key in hmap.keys():
        #     retlist.append(str(hmap[key]) + "," + str(key))

        # retlist.sort(reverse=True)
        # for i in range(len(retlist)):
        #     retlist[i] = retlist[i].split(",")[-1]
        # retlist = retlist[:k]
        # retlist.sort()
        # return retlist

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        
         