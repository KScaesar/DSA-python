import heapq


class MedianFinder:
    # https://leetcode.com/problems/find-median-from-data-stream/

    # 由於 python 的 heap 只有 最小heap
    # 想要實做 最大 heap
    # 只能自己加上負號 來模擬

    # 超簡潔寫法
    # https://leetcode.com/problems/find-median-from-data-stream/solutions/2995841/descriptive-solution-using-2-heaps-o-log-n-python3/?orderBy=newest_to_oldest

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        min_size = len(self.min_heap)
        max_size = len(self.max_heap)
        min_top = self.min_heap[0] if min_size else float('inf')
        max_top = -self.max_heap[0] if max_size else float('-inf')

        # 如果情境是兩個 heap 都可以放入
        # 統一放入 min_heap
        if max_top <= num <= min_top:
            heapq.heappush(self.min_heap, num)
            min_size += 1
        elif num > min_top:
            heapq.heappush(self.min_heap, num)
            min_size += 1
        elif num < max_top:
            heapq.heappush(self.max_heap, -num)
            max_size += 1

        # 進行再平衡
        # 不然會有某一個 heap 特別長
        if abs(min_size - max_size) <= 1:
            return

        _remove = None
        _add = None
        if min_size < max_size:
            _remove = self.max_heap
            _add = self.min_heap
        else:
            _remove = self.min_heap
            _add = self.max_heap

        element = heapq.heappop(_remove)
        heapq.heappush(_add, -element)

    def findMedian(self) -> float:
        min_size = len(self.min_heap)
        max_size = len(self.max_heap)

        if min_size == 0 or max_size == 0:
            return self.min_heap[0] if min_size != 0 \
                else -self.max_heap[0]

        elif min_size != 0 and max_size != 0 and min_size != max_size:
            return self.min_heap[0] if min_size > max_size \
                else -self.max_heap[0]

        elif min_size != 0 and max_size != 0 and min_size == max_size:
            return (self.min_heap[0] + -self.max_heap[0]) / 2


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
