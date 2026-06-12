class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        for i in s:
            arr[ord(i)-ord('a')]+= 1
        for j in t:
            arr[ord(j)-ord('a')]-= 1
        
        print(not any(arr))
        
        return not any(arr)