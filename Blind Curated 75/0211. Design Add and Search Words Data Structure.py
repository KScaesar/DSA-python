import collections


class WordDictionary:
    # https://leetcode.com/problems/design-add-and-search-words-data-structure/

    # Trie 的 應用題

    # 同樣的邏輯 都用 遞迴 dfs 撰寫
    # 用 go 寫, 不會 timeout
    # 用 py 寫, 會 timeout, 除非改成 迭代 形式

    # 寫成 迭代解法 很不順 要練習

    def __init__(self):
        self.is_word = False
        self.child: dict[str, WordDictionary] = collections.defaultdict(WordDictionary)

    def addWord(self, word: str) -> None:
        root = self
        for i in range(len(word)):
            c = word[i]
            child = root.child[c]
            root = child
        root.is_word = True

    def search(self, word: str) -> bool:
        root = self
        for i in range(len(word)):
            c = word[i]
            if c != '.':
                if c not in root.child:
                    return False
                root = root.child[c]
            else:
                # 重點 start 要在仔細想想 如何寫
                for child in root.child.values():
                    if child.search(word[i + 1:]):
                        return True
                return False
                # 重點 end

        return root.is_word

    def addWord_v1(self, word: str) -> None:
        if len(word) == 0:
            self.is_word = True
            return

        c = word[0]
        self.child[c].addWord_v1(word[1:])

    def search_v1(self, word: str) -> bool:
        if len(word) == 0:
            return self.is_word

        c = word[0]
        if c != '.':
            return self.child[c].search_v1(word[1:])
        else:
            for d in self.child.values():
                if d.search_v1(word[1:]):
                    return True
            return False


if __name__ == '__main__':
    obj2 = WordDictionary()
    # print(" addWord bad", obj2.addWord("bad"))
    # print(" addWord dad", obj2.addWord("dad"))
    # print(" addWord mad", obj2.addWord("mad"))
    # print(" search pad", obj2.search("pad"))
    # print(" search bad", obj2.search("bad"))
    # print(" search .ad", obj2.search(".ad"))
    # print(" search b..", obj2.search("b.."))

    print(obj2.addWord("a"))
    print(obj2.addWord("a"))
    print(obj2.search("a"))
    print(obj2.search("aa"))
    print(obj2.search("a."))
    print(obj2.search(".a"))
    print()
