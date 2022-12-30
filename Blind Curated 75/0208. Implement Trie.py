class Trie:
    # https://leetcode.com/problems/implement-trie-prefix-tree/

    def __init__(self):
        self.is_word = False
        self.child: dict[str, Trie] = dict()
        pass

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.is_word = True
            return

        c = word[0]
        if c in self.child.keys():
            self.child[c].insert(word[1:])
        else:
            self.child[c] = Trie()
            self.child[c].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.is_word

        c = word[0]
        if c in self.child.keys():
            return self.child[c].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True

        c = prefix[0]
        if c in self.child.keys():
            return self.child[c].startsWith(prefix[1:])
        else:
            return False


if __name__ == '__main__':
    trie = Trie()
    print("insert apple", trie.insert("apple"))
    print("search apple", trie.search("apple"))
    print("search app", trie.search("app"))
    print("start app", trie.startsWith("app"))
    print("insert app", trie.insert("app"))
    print("search app", trie.search("app"))
