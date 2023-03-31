from typing import List


class Solution:
    # https://leetcode.com/problems/group-anagrams/

    # 沒難度 複習可跳過
    def groupAnagrams_v1(self, strs: List[str]) -> List[List[str]]:
        # O( N * K*logK )
        groups = dict()

        for word in strs:
            # group = tuple(sorted([c for c in word]))
            group = tuple(sorted(word))
            if group in groups:
                groups[group].append(word)
            else:
                groups[group] = [word]

        return list(groups.values())

    def groupAnagrams_v2(self, strs: List[str]) -> List[List[str]]:
        # https://hello-kirby.hashnode.dev/leetcode-48group-anagrams

        # O( N * K )

        memo = dict()
        ord_a = ord('a')
        for idx, word in enumerate(strs):
            count = [0 for _ in range(26)]
            for char in word:
                count[ord(char) - ord_a] += 1

            # 次數超過 10, 此方法無效,
            # 比如 某個字母 次數 10
            # 會搞錯以為
            # 是 兩個字母 分別是次數 1 跟 0
            # key = "".join([str(v) for v in count])

            key = "".join([str(f'{chr(ord_a + i)}{v}') for i, v in enumerate(count)])
            print(f'{idx} {word} {count} {key}')

            if not memo.get(key):
                memo[key] = [word]
            else:
                memo[key].append(word)

        return [group for group in memo.values()]


if __name__ == '__main__':
    # print(Solution().groupAnagrams_v1(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(Solution().groupAnagrams_v2(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(Solution().groupAnagrams_v2(["bdddddddddd", "bbbbbbbbbbc"]))
