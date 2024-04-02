from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt =1
        chars.append('-1')
        s= []
        if len(chars)==1: return 1
        for i in range(1,len(chars)):
            if chars[i] == chars[i-1]:
                cnt+=1
            else:
                s.append(chars[i-1])
                if cnt > 1:
                    s.append(str(cnt))
                cnt=1
        s = str(''.join(s))
        chars.clear()
        for char in s:
            chars.append(char)
        return len(s)
