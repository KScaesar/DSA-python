import queue


class MedianFinder:
    # https://leetcode.com/problems/find-median-from-data-stream/

    def __init__(self):
        self.count = 0
        self.min_heap = queue.PriorityQueue()
        self.max_heap = queue.PriorityQueue()

    def max_heap_peek(self):
        return -self.max_heap.queue[0]

    def max_heap_get(self):
        return -self.max_heap.get()

    def max_heap_put(self, num):
        self.max_heap.put(-num)

    def addNum(self, num: int) -> None:
        # 往堆積中插入元素需要 O(logN) 時間
        # https://blog.techbridge.cc/2020/03/15/leetcode-%E5%88%B7%E9%A1%8C-pattern-two-heaps/
        # https://hackmd.io/@Hsins/two-heaps#%E4%BE%8B%E9%A1%8C-Find-the-Median-of-a-Number-Stream

        # 先進行 add 判斷
        # 最後才執行平衡
        #
        # 之前失敗的原因是
        # 想要先考慮平衡, 再進行 add 判斷
        # 同時考慮兩者, 程式太複雜

        self.count += 1

        # 反正 nums 只有兩個地方可以放
        # 先確定其中一個 情境
        # 之後靠 平衡機制
        if not self.min_heap.empty() and self.min_heap.queue[0] < num:
            self.min_heap.put(num)
        else:
            self.max_heap_put(num)

        if not self.is_balance():
            # make balance
            if self.min_heap.qsize() > self.max_heap.qsize():
                self.max_heap_put(self.min_heap.get())
            else:
                self.min_heap.put(self.max_heap_get())

    def is_balance(self) -> bool:
        min_qsize = self.min_heap.qsize()
        max_qsize = self.max_heap.qsize()
        return min_qsize == max_qsize or abs(min_qsize - max_qsize) == 1

    def findMedian(self) -> float:
        top_min = self.min_heap.queue[0] if not self.min_heap.empty() else None
        top_max = self.max_heap_peek() if not self.max_heap.empty() else None

        if self.count <= 1:
            return top_max if top_max is not None else top_min

        if self.count % 2 == 0:
            return top_max + (top_min - top_max) / 2
        else:
            # 其他作法, add 的時候
            # 可以另某一邊的 heap 數量, 總是大於另一邊
            # 這樣只要回傳 比較長的一方
            # https://hackmd.io/@Hsins/two-heaps#%E4%BE%8B%E9%A1%8C-Find-the-Median-of-a-Number-Stream
            if self.min_heap.qsize() > self.max_heap.qsize():
                return top_min
            else:
                return top_max

    def addNum_fail(self, num: int) -> None:
        # 此方法會造成 某一端的 heap 不斷成長

        top_min = self.min_heap.queue[0] if not self.min_heap.empty() else None
        top_max = self.max_heap.queue[0] * -1 if not self.max_heap.empty() else None
        mid = self.findMedian()
        self.count += 1  # 必須要再 findMedian 之後, 不然執行 findMedian 會多一個元素

        # 用一個 梯形 水平切一半 來思考
        # 上面的梯形 是 max_heap
        # 下面的梯形 是 min_heap
        if top_min is not None and top_max is not None:
            if num < mid:
                self.max_heap.get()  # 避免只有某個 heap 不斷成長
                self.min_heap.put(top_max)
                self.max_heap.put(num * -1)
            elif num > mid:
                self.min_heap.get()  # 避免只有某個 heap 不斷成長
                self.max_heap.put(top_min * -1)
                self.min_heap.put(num)
            else:
                # min_heap or max_heap 都可以 隨便選一個
                self.min_heap.put(num)

        elif top_min is not None and top_max is None:
            if num > top_min:
                self.min_heap.get()  # 避免只有某個 heap 不斷成長
                self.max_heap.put(top_min * -1)
                self.min_heap.put(num)
            else:
                self.max_heap.put(num * -1)

        elif top_min is None and top_max is not None:
            if num < top_max:
                self.max_heap.get()  # 避免只有某個 heap 不斷成長
                self.min_heap.put(top_max)
                self.max_heap.put(num * -1)
            else:
                self.min_heap.put(num)

        else:
            # min_heap or max_heap 都可以 隨便選一個
            self.min_heap.put(num)

    def addNum_fail2(self, num: int) -> None:
        # 為了想要維持 兩個 heap 的平衡
        # 感覺我的實現太複雜了, 應該想錯方向

        top_min = self.min_heap.queue[0] if not self.min_heap.empty() else None
        top_max = self.max_heap.queue[0] * -1 if not self.max_heap.empty() else None
        self.count += 1

        # 用一個 梯形 水平切一半 來思考
        # 上面的梯形 是 max_heap
        # 下面的梯形 是 min_heap
        if top_min is not None and top_max is not None:
            diff = abs(self.min_heap.qsize() - self.max_heap.qsize())
            if diff <= 1:
                if num < top_max:
                    self.max_heap.put(num * -1)
                elif num > top_min:
                    self.min_heap.put(num)
                elif top_max <= num <= top_min:
                    if self.min_heap.qsize() > self.max_heap.qsize():
                        self.max_heap.put(num * -1)
                    else:
                        self.min_heap.put(num)

            else:
                if num < top_max:
                    self.max_heap.get()  # 避免只有某個 heap 不斷成長
                    self.min_heap.put(top_max)
                    self.max_heap.put(num * -1)

                elif num > top_min:
                    self.min_heap.get()  # 避免只有某個 heap 不斷成長
                    self.max_heap.put(top_min * -1)
                    self.min_heap.put(num)

                elif top_max <= num <= top_min:
                    if self.min_heap.qsize() > self.max_heap.qsize():
                        self.max_heap.put(num * -1)
                    else:
                        self.min_heap.put(num)

        elif top_min is not None and top_max is None:
            if num > top_min:
                self.min_heap.get()  # 避免只有某個 heap 不斷成長
                self.max_heap.put(top_min * -1)
                self.min_heap.put(num)
            else:
                self.max_heap.put(num * -1)

        elif top_min is None and top_max is not None:
            if num < top_max:
                self.max_heap.get()  # 避免只有某個 heap 不斷成長
                self.min_heap.put(top_max)
                self.max_heap.put(num * -1)
            else:
                self.min_heap.put(num)

        else:
            # min_heap or max_heap 都可以 隨便選一個
            self.min_heap.put(num)

    def print_heap(self):
        min_list = []
        max_list = []
        for v in range(self.min_heap.qsize()):
            min_list.append(self.min_heap.get())
        for v in range(self.max_heap.qsize()):
            max_list.append(self.max_heap_get())
        print(f"min_list={min_list}\nmax_list{max_list}")


if __name__ == '__main__':
    obj = MedianFinder()

    for v in [1, 2, 3, 5, 6, -3]:
        obj.addNum(v)
    print(f'expect= actual={obj.findMedian()}')
    obj.print_heap()
