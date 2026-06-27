class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points: return []
        pointsToOrigin = defaultdict(list)
        for point in points:
            pointsToOrigin[(math.sqrt(point[0]**2 + point[1]**2 ))].append(point)
        print(pointsToOrigin)
        sorted_dict = dict(sorted(pointsToOrigin.items()))
        print(sorted_dict)
        res = []
        while len(res) < k:
            value = sorted_dict.pop(next(iter(sorted_dict)))
            while value and len(res) < k:
                res.append(value.pop())
        print(res)
        return res
        