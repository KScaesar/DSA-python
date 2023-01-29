from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # https://leetcode.com/problems/copy-list-with-random-pointer/description/
    def copyRandomList_v3(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # space O(1)
        # https://youtu.be/OvpKeraoxW0?t=644
        # 不想浪費額外空間保持 複製節點 和 原始節點的印射關係
        # 把 複製節點保存 在 原始節點的 next

        if head is None:
            return None

        origin = head
        while origin:
            fresh = Node(origin.val)
            origin_next = origin.next
            origin.next = fresh
            fresh.next = origin_next
            origin = origin_next

        origin = head
        while origin:
            fresh = origin.next
            if origin.random:
                fresh_random = origin.random.next
                fresh.random = fresh_random

            origin_next = fresh.next
            if origin_next:
                fresh.next = origin_next.next
            origin = origin_next

        return head.next

    def copyRandomList_v2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # space O(n)

        if head is None:
            return None

        temp = dict()  # key:value = origin:fresh
        origin = head
        dummy = Node(-1)
        fresh = dummy

        while origin:
            node = Node(origin.val)
            temp[origin] = node

            fresh.next = node
            fresh = fresh.next

            origin = origin.next

        # 跟 v1 相比
        # 順序尋訪, 用原本的 list 就好
        # 不需要額外的 array 結構
        origin = head
        while origin:
            if origin.random:
                temp[origin].random = temp[origin.random]
            origin = origin.next

        return dummy.next

    def copyRandomList_v1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        temp = []  # idx:(origin,fresh)

        cursor = head
        while cursor:
            state = (cursor, Node(cursor.val))
            temp.append(state)
            cursor = cursor.next

        dummy = Node(-1)
        cursor = dummy
        for i in range(len(temp) - 1):
            origin, fresh = temp[i]
            fresh.next = temp[i + 1][1]
            for j in range(len(temp)):
                if origin.random == temp[j][0]:
                    fresh.random = temp[j][1]
            cursor.next = fresh
            cursor = cursor.next

        origin, fresh = temp[-1]
        for j in range(len(temp)):
            if origin.random == temp[j][0]:
                fresh.random = temp[j][1]
        cursor.next = fresh

        return dummy.next


if __name__ == '__main__':
    print(Solution())
