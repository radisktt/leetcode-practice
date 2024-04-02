class Solution:
    def reverseWords(self, s: str) -> str:
        ret = []
        tmp = ""
        for c in s:
            if c!=" ":
                tmp+=c
            elif tmp!="":
                ret.append(tmp)
                tmp = ""
        if tmp!="":
            ret.append(tmp)
        return " ".join(ret[::-1])
