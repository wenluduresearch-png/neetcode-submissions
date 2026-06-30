class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            temp_i = temperatures[i]
            # j = i + 1
            days = 0
            for j in range(i + 1, len(temperatures), 1):
                days += 1
                if temperatures[j] > temp_i: break
                    
            if j == len(temperatures) - 1 and temp_i  >= temperatures[j]:
                res.append(0)

            else:
                res.append(days)
        return res