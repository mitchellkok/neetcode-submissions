class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach 1: Brute Force

        # input: list of strings
        # output: list of list of strings. Each sublist is list of anagrams (i.e. same letters, lowercase)

        # we want to use a hashmap to store the character composition for each word
        hmap = {} # each key is list of 26 ints, value is a list of words
        
        for word in strs:
            # print(word)
            tmplist = ["0"] * 26
            for i in range(len(word)):
                idx = ord(word[i]) - ord("a")
                newval = int(tmplist[idx]) + 1
                # print(".  ", idx, newval)
                tmplist[idx] = str(newval)

            key = ",".join(tmplist)
            if key in hmap.keys():
                hmap[key].append(word)
            else:
                hmap[key] = [word]

        retlist = []
        for value in hmap.values():
            retlist.append(value)

        return retlist


