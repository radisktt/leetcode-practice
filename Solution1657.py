class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dic1 = {}
        for c in word1:
            if(c in dic1):
                dic1[c]+=1
            else:
                dic1[c] =1
        dic2 = {}
        for c in word2:
            if(c in dic2):
                dic2[c]+=1
            else:
                dic2[c] =1
        for i in dic1.values():
            if i not in dic2.values():
                return False
            if sum(1 for x in dic1.values() if i==x) !=sum(1 for x in dic2.values() if i==x):
                return False
        for c in dic2.keys():
            if c not in dic1.keys():
                return False
        return True
