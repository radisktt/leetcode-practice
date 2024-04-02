from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0,0);flowerbed.append(0)
        cnt = 0
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1] == 0 :
                flowerbed[i]=1
                cnt +=1
            if cnt >=n : return True
        return cnt >= n