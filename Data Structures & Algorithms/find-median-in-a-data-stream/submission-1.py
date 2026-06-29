class MedianFinder:

    def __init__(self):
        self.lhalf = []
        self.rhalf = []


    def addNum(self, num: int) -> None:
        if self.rhalf and num > self.rhalf[0]:
            heapq.heappush(self.rhalf, num)
        else:
            heapq.heappush(self.lhalf, -1 * num)
        
        if len(self.lhalf) > len(self.rhalf) + 1:
            val = heapq.heappop(self.lhalf) * -1
            heapq.heappush(self.rhalf, val)
        if len(self.rhalf) > len(self.lhalf) + 1:
            val = heapq.heappop(self.rhalf)
            heapq.heappush(self.lhalf, -val)

    def findMedian(self) -> float:
        if len(self.lhalf) > len(self.rhalf):
            return -self.lhalf[0]
        elif len(self.rhalf) > len(self.lhalf):
            return self.rhalf[0]
        return (-self.lhalf[0] + self.rhalf[0]) / 2.0
        