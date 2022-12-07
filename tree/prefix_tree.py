from tool import *


@dataclass
class Trie:
    # https://leetcode.com/problems/implement-trie-prefix-tree/

    # 一開始，trie tree 起始於一個空的 root
    # 造成 start 和 node 差距 一個身位
    # https://hackmd.io/@sysprog/BkE3uSvdN
    def __init__(self):
        self.is_word: bool = False
        # self.child: list[Optional['Trie']] = [None] * 26
        self.child: dict[int, 'Trie'] = dict()

        # optional
        self.count_prefix: int = 0
        self.count_word: int = 0

    def insert(self, word: str) -> None:
        return self.__insert(word, 0)

    def __insert(self, word: str, start: int):
        if start == len(word):
            self.is_word = True
            return

        letter = ord(word[start]) - ord('a')
        # node = self.child[letter]
        node = self.child.get(letter)
        if node is None:
            self.child[letter] = Trie()
            node = self.child[letter]

        node.__insert(word, start + 1)

    def search(self, word: str) -> bool:
        return self.__search(word, 0)

    def __search(self, word: str, start: int) -> bool:
        if start == len(word):
            return self.is_word

        letter = ord(word[start]) - ord('a')
        # node = self.child[letter]
        node = self.child.get(letter)
        if node is None:
            return False

        # 應該用下一個節點去尋找
        # 而不是用自身節點
        # return self.__search(word, start + 1)
        return node.__search(word, start + 1)

    def startsWith(self, prefix: str) -> bool:
        return self.__startsWith(prefix, 0)

    # @debug_helper
    def __startsWith(self, prefix: str, start: int) -> bool:
        if start == len(prefix):
            return True

        letter = ord(prefix[start]) - ord('a')
        # node = self.child[letter]
        node = self.child.get(letter)
        if node is None:
            return False

        return node.__startsWith(prefix, start + 1)


if __name__ == '__main__':
    obj = Trie()
    obj.insert('apple')
    print(f'{obj.search("apple")} {obj.startsWith("ap")} {obj.startsWith("apl")}')
