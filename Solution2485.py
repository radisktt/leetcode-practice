class Solution:
    def pivotInteger(self, n: int) -> int:
        pref = 0
        total = (n*n+1)/2
        for i in range(1,n+1):
            pref+=i
            if pref == total + i - pref:
                return i
            if pref > total/2:
                break
        return -1