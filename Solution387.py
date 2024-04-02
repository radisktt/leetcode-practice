from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = Counter(s)
        print(dict.most_common()[-1][0])
        if dict.most_common()[-1][1] > 1: return -1
        else:
            for i in range(len(s)):
                if(dict[s[i]] == 1) :
                    return i
        return -1