class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s))
            ret += "~"
            ret += s
            ret += "`"
        return ret

    def decode(self, s: str) -> List[str]:
        # we need to parse the delimited string
        ret = []
        i = -1
        numbuild = True
        length = ""
        word = ""
        while i < len(s)-1:
            i += 1
            if s[i] == "~":
                # end of length, ready to build word
                word = ""
                numbuild = False
                continue
            elif s[i] == "`":
                # end of word, ready to build length
                ret.append(word)
                length = ""
                numbuild = True
                continue

            # get length
            if numbuild:
                length += s[i]
            else:
                word += s[i]            
                
        return ret
