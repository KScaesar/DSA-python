import collections
from typing import List

import tool


class Solution:
    # https://leetcode.com/problems/word-search-ii/

    # 類似 0079. Word Search

    # 2d 維度 dfs, 想利用 cache, memo 減少重複路徑的情況
    # 卻一直想不到怎麼寫, 太難了
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n, k = len(board), len(board[0]), len(words)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = set()

        # v1 v2 原本 dfs 中的 target 是用 string 儲存
        # 現在改用 trie
        trie = Trie()
        for word in words:
            trie.insert(word)
        target_count = 0

        def dfs(board, row, col, track, target: Trie):
            nonlocal target_count
            c = board[row][col]
            if c not in target.child.keys() or c == "-1" or target_count == k:
                return

            tool.print_matrix(board, row=row, col=col, track=track)

            if target.child[c].is_word and track not in ans:
                ans.add(track)
                target_count += 1
                # return # 不需要 return, tire 後面可能有更長的 word

            board[row][col] = "-1"
            for d in directions:
                y, x = row + d[0], col + d[1]
                if 0 <= y < m and 0 <= x < n:
                    dfs(board, y, x, track + board[y][x], target.child[c])
            board[row][col] = c

            # len(target.child[c].child) == 0
            # 判斷 target.child[c] 是否為 結尾節點, 沒有其他 word 會使用到
            # 是的話就刪除該節點
            # 能夠到達該節點, 表示已經順利找到 目標 word
            #
            # 如果不進行刪除, 會造成多餘的走訪
            # 比如說 某次 dfs 經過 (x1,y1) 最後到達 (x2,y2) 發現目標 word1
            # dfs 回退的過程又來到 (x1,y1)
            # 有另一個路徑 (x1,y1) -> (x3,y3) 可以發現 word1
            # 到了 (x3,y3) 才發現, word1 已經被寫入到答案, 於是又回退 到 (x1,y1)
            #
            # 如果在第一次發現 目標 word 的時候, 就刪除節點
            # 可以避免回退的過程, 重複走訪
            if len(target.child[c].child) == 0:
                target.child.pop(c)

        for row in range(m):
            for col in range(n):
                dfs(board, row, col, board[row][col], trie)

        return list(ans)

    def findWords_fail(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 想複用中間結果, 會卡在不知道哪邊尋訪過
        # 如果只紀錄 開始點 結束點 目標值, 無法標記 -1 作為提示
        #
        # 本實作 無法有正常結果
        # 只是留下 失敗紀錄 便於日後回想

        m, n, k = len(board), len(board[0]), len(words)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = []

        found = {word: False for word in words}

        paths = collections.defaultdict(tuple)

        # @tool.debug_helper
        def dfs(board, start, cursor, track, word, **helper):
            for i in range(len(word)):
                if (cursor, word[i:]) in paths:
                    print("paths", cursor, word[i:], paths)
                    cursor = paths[(cursor, word[i:])]
                    track = word[i:]

            row = cursor[0]
            col = cursor[1]
            paths[(cursor, "".join(list(reversed(track))))] = start

            if track != word[:len(track)]:
                return

            tool.print_matrix(board, row=row, col=col, track=track, word=word, indent=helper.get("indent"))

            if track == word:
                ans.append(word)
                found[word] = True
                return

            c = board[row][col]
            board[row][col] = "-1"

            for d in directions:
                y = row + d[0]
                x = col + d[1]
                if y < 0 or y == m or x < 0 or x == n:
                    continue
                if board[y][x] == "-1" or found[word]:
                    continue

                dfs(board, start, (y, x), track + board[y][x], word)

            board[row][col] = c

        for row in range(m):
            for col in range(n):
                head = board[row][col]
                for word in words:
                    if not found[word]:
                        dfs(board, (row, col), (row, col), head, word)

        return ans

    def findWords_timeout_v2(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n, k = len(board), len(board[0]), len(words)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = []

        found = {word: False for word in words}

        # @tool.debug_helper
        def dfs(board, row, col, track, k_start, **helper):
            target = words[k_start]
            if board[row][col] == "-1" or found[target]:
                return

            if track != target[:len(track)]:
                return

            tool.print_matrix(board, row=row, col=col, track=track, target=target, indent=helper.get("indent"))

            if track == target:
                ans.append(target)
                found[target] = True
                return

            c = board[row][col]
            board[row][col] = "-1"

            # 跟 timeout_v1 版本的差異
            # 原本以為 當到達 target 結尾
            # 之後只要替換 後面幾個字符, 就可以快速判斷 不同的 word
            # 但是卻忘記了
            # 想要到達結尾, 表示前段字符 也要經過相同的次數的 word 判斷
            # 總體時間並沒有比較快
            for i in range(k_start, k):
                for d in directions:
                    y = row + d[0]
                    x = col + d[1]
                    if y < 0 or y == m or x < 0 or x == n:
                        continue
                    dfs(board, y, x, track + board[y][x], i)

            board[row][col] = c

        for row in range(m):
            for col in range(n):
                for i in range(k):
                    head = board[row][col]
                    dfs(board, row, col, head, i)

        return ans

    def findWords_timeout_v1(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n, k = len(board), len(board[0]), len(words)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = []

        # 如果遇到多個目標的前綴相同, dict set, 無法保證取出哪一個 word
        # mapper = {word[0]: word for word in words}
        # targets = set(mapper.keys())

        found = {word: False for word in words}

        memo = set()

        # @tool.debug_helper
        def dfs(board, row, col, track, target, **helper):
            if board[row][col] == "-1" or found[target]:
                return
            if track != target[:len(track)]:
                return

            tool.print_matrix(board, row=row, col=col, track=track, target=target, indent=helper.get("indent"))

            if track == target:
                ans.append(target)
                found[target] = True
                return

            c = board[row][col]
            board[row][col] = "-1"

            for d in directions:
                y = row + d[0]
                x = col + d[1]
                if y < 0 or y == m or x < 0 or x == n:
                    continue

                # 原本想利用 memo 處理重複字串的情況, 來避免 timeout
                # 但 2d 空間有太多可能
                # 總是會漏一些情境沒考慮到
                #
                # from_to = ((row, col), (y, x), track + board[y][x], target)
                # if from_to in memo:
                #     continue
                # memo.add(from_to)

                dfs(board, y, x, track + board[y][x], target)

            board[row][col] = c

        for row in range(m):
            for col in range(n):
                head = board[row][col]

                # 如果遇到多個目標的前綴相同, dict set, 無法保證取出哪一個 word
                # if head in targets:
                #     word = mapper[head]
                #     if not found[word]:
                #         dfs(board, row, col, head, word)

                for word in words:
                    if word[0] == head and not found[word]:
                        dfs(board, row, col, head, word)

        return ans


class Trie:
    def __init__(self):
        self.is_word = False
        self.child: dict[str, Trie] = collections.defaultdict(Trie)

    def insert(self, word):
        root = self
        for c in word:
            child = root.child[c]
            root = child
        root.is_word = True

    def insert_v1(self, word):
        if len(word) == 0:
            self.is_word = True
            return

        c = word[0]
        self.child[c].insert_v1(word[1:])


if __name__ == '__main__':
    # board1 = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    # print(Solution().findWords(board1, ["oath", "pea", "eat", "rain"]))

    board2 = [["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]]
    print(Solution().findWords(board2, ["oa", "oaa"]))

    # board3 = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    # print(Solution().findWords(board3, ["oath", "pea", "eat", "rain", "hklf", "hf"]))

    # board4 = [["a", "b", "c", "e"], ["z", "z", "d", "z"], ["z", "z", "c", "z"], ["z", "a", "b", "z"]]
    # print(Solution().findWords(board4, ["abcdce"]))

    # board5 = [["e", "e", "c", "d", "b", "b", "c", "b", "c", "d", "e"], ["c", "e", "e", "a", "d", "d", "e", "c", "c", "c", "b"],
    #           ["b", "e", "a", "c", "d", "a", "a", "b", "c", "d", "c"], ["e", "d", "e", "d", "c", "c", "e", "b", "d", "e", "e"],
    #           ["b", "b", "b", "a", "b", "d", "b", "b", "b", "a", "a"], ["e", "e", "b", "e", "c", "c", "a", "b", "e", "e", "c"],
    #           ["b", "a", "b", "c", "b", "d", "a", "d", "c", "d", "a"], ["d", "b", "a", "e", "a", "c", "e", "a", "d", "e", "c"]]
    # print(Solution().findWords(board5, ["aeceecbee"]))

    # board6 = [["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
    #           ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
    #           ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
    #           ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
    #           ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"]]
    # print(Solution().findWords(board6, ["ababababaa", "ababababab", "ababababac", "ababababad", "ababababae", "ababababaf", "ababababag",
    #                                     "ababababah", "ababababai", "ababababaj", "ababababak", "ababababal", "ababababam", "ababababan",
    #                                     "ababababao", "ababababap", "ababababaq", "ababababar", "ababababas", "ababababat", "ababababau",
    #                                     "ababababav", "ababababaw", "ababababax", "ababababay", "ababababaz", "ababababba", "ababababbb",
    #                                     "ababababbc", "ababababbd", "ababababbe", "ababababbf", "ababababbg", "ababababbh", "ababababbi",
    #                                     "ababababbj", "ababababbk", "ababababbl", "ababababbm", "ababababbn", "ababababbo", "ababababbp",
    #                                     "ababababbq", "ababababbr", "ababababbs", "ababababbt", "ababababbu", "ababababbv", "ababababbw",
    #                                     "ababababbx", "ababababby", "ababababbz", "ababababca", "ababababcb", "ababababcc", "ababababcd",
    #                                     "ababababce", "ababababcf", "ababababcg", "ababababch", "ababababci", "ababababcj", "ababababck",
    #                                     "ababababcl", "ababababcm", "ababababcn", "ababababco", "ababababcp", "ababababcq", "ababababcr",
    #                                     "ababababcs", "ababababct", "ababababcu", "ababababcv", "ababababcw", "ababababcx", "ababababcy",
    #                                     "ababababcz", "ababababda", "ababababdb", "ababababdc", "ababababdd", "ababababde", "ababababdf",
    #                                     "ababababdg", "ababababdh", "ababababdi", "ababababdj", "ababababdk", "ababababdl", "ababababdm",
    #                                     "ababababdn", "ababababdo", "ababababdp", "ababababdq", "ababababdr", "ababababds", "ababababdt",
    #                                     "ababababdu", "ababababdv", "ababababdw", "ababababdx", "ababababdy", "ababababdz", "ababababea",
    #                                     "ababababeb", "ababababec", "ababababed", "ababababee", "ababababef", "ababababeg", "ababababeh",
    #                                     "ababababei", "ababababej", "ababababek", "ababababel", "ababababem", "ababababen", "ababababeo",
    #                                     "ababababep", "ababababeq", "ababababer", "ababababes", "ababababet", "ababababeu", "ababababev",
    #                                     "ababababew", "ababababex", "ababababey", "ababababez", "ababababfa", "ababababfb", "ababababfc",
    #                                     "ababababfd", "ababababfe", "ababababff", "ababababfg", "ababababfh", "ababababfi", "ababababfj",
    #                                     "ababababfk", "ababababfl", "ababababfm", "ababababfn", "ababababfo", "ababababfp", "ababababfq",
    #                                     "ababababfr", "ababababfs", "ababababft", "ababababfu", "ababababfv", "ababababfw", "ababababfx",
    #                                     "ababababfy", "ababababfz", "ababababga", "ababababgb", "ababababgc", "ababababgd", "ababababge",
    #                                     "ababababgf", "ababababgg", "ababababgh", "ababababgi", "ababababgj", "ababababgk", "ababababgl",
    #                                     "ababababgm", "ababababgn", "ababababgo", "ababababgp", "ababababgq", "ababababgr", "ababababgs",
    #                                     "ababababgt", "ababababgu", "ababababgv", "ababababgw", "ababababgx", "ababababgy", "ababababgz",
    #                                     "ababababha", "ababababhb", "ababababhc", "ababababhd", "ababababhe", "ababababhf", "ababababhg",
    #                                     "ababababhh", "ababababhi", "ababababhj", "ababababhk", "ababababhl", "ababababhm", "ababababhn",
    #                                     "ababababho", "ababababhp", "ababababhq", "ababababhr", "ababababhs", "ababababht", "ababababhu",
    #                                     "ababababhv", "ababababhw", "ababababhx", "ababababhy", "ababababhz", "ababababia", "ababababib",
    #                                     "ababababic", "ababababid", "ababababie", "ababababif", "ababababig", "ababababih", "ababababii",
    #                                     "ababababij", "ababababik", "ababababil", "ababababim", "ababababin", "ababababio", "ababababip",
    #                                     "ababababiq", "ababababir", "ababababis", "ababababit", "ababababiu", "ababababiv", "ababababiw",
    #                                     "ababababix", "ababababiy", "ababababiz", "ababababja", "ababababjb", "ababababjc", "ababababjd",
    #                                     "ababababje", "ababababjf", "ababababjg", "ababababjh", "ababababji", "ababababjj", "ababababjk",
    #                                     "ababababjl", "ababababjm", "ababababjn", "ababababjo", "ababababjp", "ababababjq", "ababababjr",
    #                                     "ababababjs", "ababababjt", "ababababju", "ababababjv", "ababababjw", "ababababjx", "ababababjy",
    #                                     "ababababjz", "ababababka", "ababababkb", "ababababkc", "ababababkd", "ababababke", "ababababkf",
    #                                     "ababababkg", "ababababkh", "ababababki", "ababababkj", "ababababkk", "ababababkl", "ababababkm",
    #                                     "ababababkn", "ababababko", "ababababkp", "ababababkq", "ababababkr", "ababababks", "ababababkt",
    #                                     "ababababku", "ababababkv", "ababababkw", "ababababkx", "ababababky", "ababababkz", "ababababla",
    #                                     "abababablb", "abababablc", "ababababld", "abababable", "abababablf", "abababablg", "abababablh",
    #                                     "ababababli", "abababablj", "abababablk", "ababababll", "abababablm", "ababababln", "abababablo",
    #                                     "abababablp", "abababablq", "abababablr", "ababababls", "abababablt", "abababablu", "abababablv",
    #                                     "abababablw", "abababablx", "abababably", "abababablz", "ababababma", "ababababmb", "ababababmc",
    #                                     "ababababmd", "ababababme", "ababababmf", "ababababmg", "ababababmh", "ababababmi", "ababababmj",
    #                                     "ababababmk", "ababababml", "ababababmm", "ababababmn", "ababababmo", "ababababmp", "ababababmq",
    #                                     "ababababmr", "ababababms", "ababababmt", "ababababmu", "ababababmv", "ababababmw", "ababababmx",
    #                                     "ababababmy", "ababababmz", "ababababna", "ababababnb", "ababababnc", "ababababnd", "ababababne",
    #                                     "ababababnf", "ababababng", "ababababnh", "ababababni", "ababababnj", "ababababnk", "ababababnl",
    #                                     "ababababnm", "ababababnn", "ababababno", "ababababnp", "ababababnq", "ababababnr", "ababababns",
    #                                     "ababababnt", "ababababnu", "ababababnv", "ababababnw", "ababababnx", "ababababny", "ababababnz",
    #                                     "ababababoa", "ababababob", "ababababoc", "ababababod", "ababababoe", "ababababof", "ababababog",
    #                                     "ababababoh", "ababababoi", "ababababoj", "ababababok", "ababababol", "ababababom", "ababababon",
    #                                     "ababababoo", "ababababop", "ababababoq", "ababababor", "ababababos", "ababababot", "ababababou",
    #                                     "ababababov", "ababababow", "ababababox", "ababababoy", "ababababoz", "ababababpa", "ababababpb",
    #                                     "ababababpc", "ababababpd", "ababababpe", "ababababpf", "ababababpg", "ababababph", "ababababpi",
    #                                     "ababababpj", "ababababpk", "ababababpl", "ababababpm", "ababababpn", "ababababpo", "ababababpp",
    #                                     "ababababpq", "ababababpr", "ababababps", "ababababpt", "ababababpu", "ababababpv", "ababababpw",
    #                                     "ababababpx", "ababababpy", "ababababpz", "ababababqa", "ababababqb", "ababababqc", "ababababqd",
    #                                     "ababababqe", "ababababqf", "ababababqg", "ababababqh", "ababababqi", "ababababqj", "ababababqk",
    #                                     "ababababql", "ababababqm", "ababababqn", "ababababqo", "ababababqp", "ababababqq", "ababababqr",
    #                                     "ababababqs", "ababababqt", "ababababqu", "ababababqv", "ababababqw", "ababababqx", "ababababqy",
    #                                     "ababababqz", "ababababra", "ababababrb", "ababababrc", "ababababrd", "ababababre", "ababababrf",
    #                                     "ababababrg", "ababababrh", "ababababri", "ababababrj", "ababababrk", "ababababrl", "ababababrm",
    #                                     "ababababrn", "ababababro", "ababababrp", "ababababrq", "ababababrr", "ababababrs", "ababababrt",
    #                                     "ababababru", "ababababrv", "ababababrw", "ababababrx", "ababababry", "ababababrz", "ababababsa",
    #                                     "ababababsb", "ababababsc", "ababababsd", "ababababse", "ababababsf", "ababababsg", "ababababsh",
    #                                     "ababababsi", "ababababsj", "ababababsk", "ababababsl", "ababababsm", "ababababsn", "ababababso",
    #                                     "ababababsp", "ababababsq", "ababababsr", "ababababss", "ababababst", "ababababsu", "ababababsv",
    #                                     "ababababsw", "ababababsx", "ababababsy", "ababababsz", "ababababta", "ababababtb", "ababababtc",
    #                                     "ababababtd", "ababababte", "ababababtf", "ababababtg", "ababababth", "ababababti", "ababababtj",
    #                                     "ababababtk", "ababababtl", "ababababtm", "ababababtn", "ababababto", "ababababtp", "ababababtq",
    #                                     "ababababtr", "ababababts", "ababababtt", "ababababtu", "ababababtv", "ababababtw", "ababababtx",
    #                                     "ababababty", "ababababtz", "ababababua", "ababababub", "ababababuc", "ababababud", "ababababue",
    #                                     "ababababuf", "ababababug", "ababababuh", "ababababui", "ababababuj", "ababababuk", "ababababul",
    #                                     "ababababum", "ababababun", "ababababuo", "ababababup", "ababababuq", "ababababur", "ababababus",
    #                                     "ababababut", "ababababuu", "ababababuv", "ababababuw", "ababababux", "ababababuy", "ababababuz",
    #                                     "ababababva", "ababababvb", "ababababvc", "ababababvd", "ababababve", "ababababvf", "ababababvg",
    #                                     "ababababvh", "ababababvi", "ababababvj", "ababababvk", "ababababvl", "ababababvm", "ababababvn",
    #                                     "ababababvo", "ababababvp", "ababababvq", "ababababvr", "ababababvs", "ababababvt", "ababababvu",
    #                                     "ababababvv", "ababababvw", "ababababvx", "ababababvy", "ababababvz", "ababababwa", "ababababwb",
    #                                     "ababababwc", "ababababwd", "ababababwe", "ababababwf", "ababababwg", "ababababwh", "ababababwi",
    #                                     "ababababwj", "ababababwk", "ababababwl", "ababababwm", "ababababwn", "ababababwo", "ababababwp",
    #                                     "ababababwq", "ababababwr", "ababababws", "ababababwt", "ababababwu", "ababababwv", "ababababww",
    #                                     "ababababwx", "ababababwy", "ababababwz", "ababababxa", "ababababxb", "ababababxc", "ababababxd",
    #                                     "ababababxe", "ababababxf", "ababababxg", "ababababxh", "ababababxi", "ababababxj", "ababababxk",
    #                                     "ababababxl", "ababababxm", "ababababxn", "ababababxo", "ababababxp", "ababababxq", "ababababxr",
    #                                     "ababababxs", "ababababxt", "ababababxu", "ababababxv", "ababababxw", "ababababxx", "ababababxy",
    #                                     "ababababxz", "ababababya", "ababababyb", "ababababyc", "ababababyd", "ababababye", "ababababyf",
    #                                     "ababababyg", "ababababyh", "ababababyi", "ababababyj", "ababababyk", "ababababyl", "ababababym",
    #                                     "ababababyn", "ababababyo", "ababababyp", "ababababyq", "ababababyr", "ababababys", "ababababyt",
    #                                     "ababababyu", "ababababyv", "ababababyw", "ababababyx", "ababababyy", "ababababyz", "ababababza",
    #                                     "ababababzb", "ababababzc", "ababababzd", "ababababze", "ababababzf", "ababababzg", "ababababzh",
    #                                     "ababababzi", "ababababzj", "ababababzk", "ababababzl", "ababababzm", "ababababzn", "ababababzo",
    #                                     "ababababzp", "ababababzq", "ababababzr", "ababababzs", "ababababzt", "ababababzu", "ababababzv",
    #                                     "ababababzw", "ababababzx", "ababababzy", "ababababzz"]))

    # board7 = [["m", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"], ["n", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #           ["o", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["p", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #           ["q", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["r", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #           ["s", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["t", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #           ["u", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["v", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #           ["w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["x", "y", "z", "a", "a", "a", "a", "a", "a", "a", "a", "a"]]
    # tool.print_matrix(board7)
    # print(Solution().findWords(board7, ["aaaaaaaaaa", "baaaaaaaaa", "caaaaaaaaa", "daaaaaaaaa", "eaaaaaaaaa", "faaaaaaaaa", "gaaaaaaaaa",
    #                                     "haaaaaaaaa", "iaaaaaaaaa", "jaaaaaaaaa", "kaaaaaaaaa", "laaaaaaaaa", "maaaaaaaaa", "naaaaaaaaa",
    #                                     "oaaaaaaaaa", "paaaaaaaaa", "qaaaaaaaaa", "raaaaaaaaa", "saaaaaaaaa", "taaaaaaaaa", "uaaaaaaaaa",
    #                                     "vaaaaaaaaa", "waaaaaaaaa", "xaaaaaaaaa", "yaaaaaaaaa", "zaaaaaaaaa", "abaaaaaaaa", "bbaaaaaaaa",
    #                                     "cbaaaaaaaa", "dbaaaaaaaa", "ebaaaaaaaa", "fbaaaaaaaa", "gbaaaaaaaa", "hbaaaaaaaa", "ibaaaaaaaa",
    #                                     "jbaaaaaaaa", "kbaaaaaaaa", "lbaaaaaaaa", "mbaaaaaaaa", "nbaaaaaaaa", "obaaaaaaaa", "pbaaaaaaaa",
    #                                     "qbaaaaaaaa", "rbaaaaaaaa", "sbaaaaaaaa", "tbaaaaaaaa", "ubaaaaaaaa", "vbaaaaaaaa", "wbaaaaaaaa",
    #                                     "xbaaaaaaaa", "ybaaaaaaaa", "zbaaaaaaaa", "acaaaaaaaa", "bcaaaaaaaa", "ccaaaaaaaa", "dcaaaaaaaa",
    #                                     "ecaaaaaaaa", "fcaaaaaaaa", "gcaaaaaaaa", "hcaaaaaaaa", "icaaaaaaaa", "jcaaaaaaaa", "kcaaaaaaaa",
    #                                     "lcaaaaaaaa", "mcaaaaaaaa", "ncaaaaaaaa", "ocaaaaaaaa", "pcaaaaaaaa", "qcaaaaaaaa", "rcaaaaaaaa",
    #                                     "scaaaaaaaa", "tcaaaaaaaa", "ucaaaaaaaa", "vcaaaaaaaa", "wcaaaaaaaa", "xcaaaaaaaa", "ycaaaaaaaa",
    #                                     "zcaaaaaaaa", "adaaaaaaaa", "bdaaaaaaaa", "cdaaaaaaaa", "ddaaaaaaaa", "edaaaaaaaa", "fdaaaaaaaa",
    #                                     "gdaaaaaaaa", "hdaaaaaaaa", "idaaaaaaaa", "jdaaaaaaaa", "kdaaaaaaaa", "ldaaaaaaaa", "mdaaaaaaaa",
    #                                     "ndaaaaaaaa", "odaaaaaaaa", "pdaaaaaaaa", "qdaaaaaaaa", "rdaaaaaaaa", "sdaaaaaaaa", "tdaaaaaaaa",
    #                                     "udaaaaaaaa", "vdaaaaaaaa", "wdaaaaaaaa", "xdaaaaaaaa", "ydaaaaaaaa", "zdaaaaaaaa", "aeaaaaaaaa",
    #                                     "beaaaaaaaa", "ceaaaaaaaa", "deaaaaaaaa", "eeaaaaaaaa", "feaaaaaaaa", "geaaaaaaaa", "heaaaaaaaa",
    #                                     "ieaaaaaaaa", "jeaaaaaaaa", "keaaaaaaaa", "leaaaaaaaa", "meaaaaaaaa", "neaaaaaaaa", "oeaaaaaaaa",
    #                                     "peaaaaaaaa", "qeaaaaaaaa", "reaaaaaaaa", "seaaaaaaaa", "teaaaaaaaa", "ueaaaaaaaa", "veaaaaaaaa",
    #                                     "weaaaaaaaa", "xeaaaaaaaa", "yeaaaaaaaa", "zeaaaaaaaa", "afaaaaaaaa", "bfaaaaaaaa", "cfaaaaaaaa",
    #                                     "dfaaaaaaaa", "efaaaaaaaa", "ffaaaaaaaa", "gfaaaaaaaa", "hfaaaaaaaa", "ifaaaaaaaa", "jfaaaaaaaa",
    #                                     "kfaaaaaaaa", "lfaaaaaaaa", "mfaaaaaaaa", "nfaaaaaaaa", "ofaaaaaaaa", "pfaaaaaaaa", "qfaaaaaaaa",
    #                                     "rfaaaaaaaa", "sfaaaaaaaa", "tfaaaaaaaa", "ufaaaaaaaa", "vfaaaaaaaa", "wfaaaaaaaa", "xfaaaaaaaa",
    #                                     "yfaaaaaaaa", "zfaaaaaaaa", "agaaaaaaaa", "bgaaaaaaaa", "cgaaaaaaaa", "dgaaaaaaaa", "egaaaaaaaa",
    #                                     "fgaaaaaaaa", "ggaaaaaaaa", "hgaaaaaaaa", "igaaaaaaaa", "jgaaaaaaaa", "kgaaaaaaaa", "lgaaaaaaaa",
    #                                     "mgaaaaaaaa", "ngaaaaaaaa", "ogaaaaaaaa", "pgaaaaaaaa", "qgaaaaaaaa", "rgaaaaaaaa", "sgaaaaaaaa",
    #                                     "tgaaaaaaaa", "ugaaaaaaaa", "vgaaaaaaaa", "wgaaaaaaaa", "xgaaaaaaaa", "ygaaaaaaaa", "zgaaaaaaaa",
    #                                     "ahaaaaaaaa", "bhaaaaaaaa", "chaaaaaaaa", "dhaaaaaaaa", "ehaaaaaaaa", "fhaaaaaaaa", "ghaaaaaaaa",
    #                                     "hhaaaaaaaa", "ihaaaaaaaa", "jhaaaaaaaa", "khaaaaaaaa", "lhaaaaaaaa", "mhaaaaaaaa", "nhaaaaaaaa",
    #                                     "ohaaaaaaaa", "phaaaaaaaa", "qhaaaaaaaa", "rhaaaaaaaa", "shaaaaaaaa", "thaaaaaaaa", "uhaaaaaaaa",
    #                                     "vhaaaaaaaa", "whaaaaaaaa", "xhaaaaaaaa", "yhaaaaaaaa", "zhaaaaaaaa", "aiaaaaaaaa", "biaaaaaaaa",
    #                                     "ciaaaaaaaa", "diaaaaaaaa", "eiaaaaaaaa", "fiaaaaaaaa", "giaaaaaaaa", "hiaaaaaaaa", "iiaaaaaaaa",
    #                                     "jiaaaaaaaa", "kiaaaaaaaa", "liaaaaaaaa", "miaaaaaaaa", "niaaaaaaaa", "oiaaaaaaaa", "piaaaaaaaa",
    #                                     "qiaaaaaaaa", "riaaaaaaaa", "siaaaaaaaa", "tiaaaaaaaa", "uiaaaaaaaa", "viaaaaaaaa", "wiaaaaaaaa",
    #                                     "xiaaaaaaaa", "yiaaaaaaaa", "ziaaaaaaaa", "ajaaaaaaaa", "bjaaaaaaaa", "cjaaaaaaaa", "djaaaaaaaa",
    #                                     "ejaaaaaaaa", "fjaaaaaaaa", "gjaaaaaaaa", "hjaaaaaaaa", "ijaaaaaaaa", "jjaaaaaaaa", "kjaaaaaaaa",
    #                                     "ljaaaaaaaa", "mjaaaaaaaa", "njaaaaaaaa", "ojaaaaaaaa", "pjaaaaaaaa", "qjaaaaaaaa", "rjaaaaaaaa",
    #                                     "sjaaaaaaaa", "tjaaaaaaaa", "ujaaaaaaaa", "vjaaaaaaaa", "wjaaaaaaaa", "xjaaaaaaaa", "yjaaaaaaaa",
    #                                     "zjaaaaaaaa", "akaaaaaaaa", "bkaaaaaaaa", "ckaaaaaaaa", "dkaaaaaaaa", "ekaaaaaaaa", "fkaaaaaaaa",
    #                                     "gkaaaaaaaa", "hkaaaaaaaa", "ikaaaaaaaa", "jkaaaaaaaa", "kkaaaaaaaa", "lkaaaaaaaa", "mkaaaaaaaa",
    #                                     "nkaaaaaaaa", "okaaaaaaaa", "pkaaaaaaaa", "qkaaaaaaaa", "rkaaaaaaaa", "skaaaaaaaa", "tkaaaaaaaa",
    #                                     "ukaaaaaaaa", "vkaaaaaaaa", "wkaaaaaaaa", "xkaaaaaaaa", "ykaaaaaaaa", "zkaaaaaaaa", "alaaaaaaaa",
    #                                     "blaaaaaaaa", "claaaaaaaa", "dlaaaaaaaa", "elaaaaaaaa", "flaaaaaaaa", "glaaaaaaaa", "hlaaaaaaaa",
    #                                     "ilaaaaaaaa", "jlaaaaaaaa", "klaaaaaaaa", "llaaaaaaaa", "mlaaaaaaaa", "nlaaaaaaaa", "olaaaaaaaa",
    #                                     "plaaaaaaaa", "qlaaaaaaaa", "rlaaaaaaaa", "slaaaaaaaa", "tlaaaaaaaa", "ulaaaaaaaa", "vlaaaaaaaa",
    #                                     "wlaaaaaaaa", "xlaaaaaaaa", "ylaaaaaaaa", "zlaaaaaaaa", "amaaaaaaaa", "bmaaaaaaaa", "cmaaaaaaaa",
    #                                     "dmaaaaaaaa", "emaaaaaaaa", "fmaaaaaaaa", "gmaaaaaaaa", "hmaaaaaaaa", "imaaaaaaaa", "jmaaaaaaaa",
    #                                     "kmaaaaaaaa", "lmaaaaaaaa", "mmaaaaaaaa", "nmaaaaaaaa", "omaaaaaaaa", "pmaaaaaaaa", "qmaaaaaaaa",
    #                                     "rmaaaaaaaa", "smaaaaaaaa", "tmaaaaaaaa", "umaaaaaaaa", "vmaaaaaaaa", "wmaaaaaaaa", "xmaaaaaaaa",
    #                                     "ymaaaaaaaa", "zmaaaaaaaa", "anaaaaaaaa", "bnaaaaaaaa", "cnaaaaaaaa", "dnaaaaaaaa", "enaaaaaaaa",
    #                                     "fnaaaaaaaa", "gnaaaaaaaa", "hnaaaaaaaa", "inaaaaaaaa", "jnaaaaaaaa", "knaaaaaaaa", "lnaaaaaaaa",
    #                                     "mnaaaaaaaa", "nnaaaaaaaa", "onaaaaaaaa", "pnaaaaaaaa", "qnaaaaaaaa", "rnaaaaaaaa", "snaaaaaaaa",
    #                                     "tnaaaaaaaa", "unaaaaaaaa", "vnaaaaaaaa", "wnaaaaaaaa", "xnaaaaaaaa", "ynaaaaaaaa", "znaaaaaaaa",
    #                                     "aoaaaaaaaa", "boaaaaaaaa", "coaaaaaaaa", "doaaaaaaaa", "eoaaaaaaaa", "foaaaaaaaa", "goaaaaaaaa",
    #                                     "hoaaaaaaaa", "ioaaaaaaaa", "joaaaaaaaa", "koaaaaaaaa", "loaaaaaaaa", "moaaaaaaaa", "noaaaaaaaa",
    #                                     "ooaaaaaaaa", "poaaaaaaaa", "qoaaaaaaaa", "roaaaaaaaa", "soaaaaaaaa", "toaaaaaaaa", "uoaaaaaaaa",
    #                                     "voaaaaaaaa", "woaaaaaaaa", "xoaaaaaaaa", "yoaaaaaaaa", "zoaaaaaaaa", "apaaaaaaaa", "bpaaaaaaaa",
    #                                     "cpaaaaaaaa", "dpaaaaaaaa", "epaaaaaaaa", "fpaaaaaaaa", "gpaaaaaaaa", "hpaaaaaaaa", "ipaaaaaaaa",
    #                                     "jpaaaaaaaa", "kpaaaaaaaa", "lpaaaaaaaa", "mpaaaaaaaa", "npaaaaaaaa", "opaaaaaaaa", "ppaaaaaaaa",
    #                                     "qpaaaaaaaa", "rpaaaaaaaa", "spaaaaaaaa", "tpaaaaaaaa", "upaaaaaaaa", "vpaaaaaaaa", "wpaaaaaaaa",
    #                                     "xpaaaaaaaa", "ypaaaaaaaa", "zpaaaaaaaa", "aqaaaaaaaa", "bqaaaaaaaa", "cqaaaaaaaa", "dqaaaaaaaa",
    #                                     "eqaaaaaaaa", "fqaaaaaaaa", "gqaaaaaaaa", "hqaaaaaaaa", "iqaaaaaaaa", "jqaaaaaaaa", "kqaaaaaaaa",
    #                                     "lqaaaaaaaa", "mqaaaaaaaa", "nqaaaaaaaa", "oqaaaaaaaa", "pqaaaaaaaa", "qqaaaaaaaa", "rqaaaaaaaa",
    #                                     "sqaaaaaaaa", "tqaaaaaaaa", "uqaaaaaaaa", "vqaaaaaaaa", "wqaaaaaaaa", "xqaaaaaaaa", "yqaaaaaaaa",
    #                                     "zqaaaaaaaa", "araaaaaaaa", "braaaaaaaa", "craaaaaaaa", "draaaaaaaa", "eraaaaaaaa", "fraaaaaaaa",
    #                                     "graaaaaaaa", "hraaaaaaaa", "iraaaaaaaa", "jraaaaaaaa", "kraaaaaaaa", "lraaaaaaaa", "mraaaaaaaa",
    #                                     "nraaaaaaaa", "oraaaaaaaa", "praaaaaaaa", "qraaaaaaaa", "rraaaaaaaa", "sraaaaaaaa", "traaaaaaaa",
    #                                     "uraaaaaaaa", "vraaaaaaaa", "wraaaaaaaa", "xraaaaaaaa", "yraaaaaaaa", "zraaaaaaaa", "asaaaaaaaa",
    #                                     "bsaaaaaaaa", "csaaaaaaaa", "dsaaaaaaaa", "esaaaaaaaa", "fsaaaaaaaa", "gsaaaaaaaa", "hsaaaaaaaa",
    #                                     "isaaaaaaaa", "jsaaaaaaaa", "ksaaaaaaaa", "lsaaaaaaaa", "msaaaaaaaa", "nsaaaaaaaa", "osaaaaaaaa",
    #                                     "psaaaaaaaa", "qsaaaaaaaa", "rsaaaaaaaa", "ssaaaaaaaa", "tsaaaaaaaa", "usaaaaaaaa", "vsaaaaaaaa",
    #                                     "wsaaaaaaaa", "xsaaaaaaaa", "ysaaaaaaaa", "zsaaaaaaaa", "ataaaaaaaa", "btaaaaaaaa", "ctaaaaaaaa",
    #                                     "dtaaaaaaaa", "etaaaaaaaa", "ftaaaaaaaa", "gtaaaaaaaa", "htaaaaaaaa", "itaaaaaaaa", "jtaaaaaaaa",
    #                                     "ktaaaaaaaa", "ltaaaaaaaa", "mtaaaaaaaa", "ntaaaaaaaa", "otaaaaaaaa", "ptaaaaaaaa", "qtaaaaaaaa",
    #                                     "rtaaaaaaaa", "staaaaaaaa", "ttaaaaaaaa", "utaaaaaaaa", "vtaaaaaaaa", "wtaaaaaaaa", "xtaaaaaaaa",
    #                                     "ytaaaaaaaa", "ztaaaaaaaa", "auaaaaaaaa", "buaaaaaaaa", "cuaaaaaaaa", "duaaaaaaaa", "euaaaaaaaa",
    #                                     "fuaaaaaaaa", "guaaaaaaaa", "huaaaaaaaa", "iuaaaaaaaa", "juaaaaaaaa", "kuaaaaaaaa", "luaaaaaaaa",
    #                                     "muaaaaaaaa", "nuaaaaaaaa", "ouaaaaaaaa", "puaaaaaaaa", "quaaaaaaaa", "ruaaaaaaaa", "suaaaaaaaa",
    #                                     "tuaaaaaaaa", "uuaaaaaaaa", "vuaaaaaaaa", "wuaaaaaaaa", "xuaaaaaaaa", "yuaaaaaaaa", "zuaaaaaaaa",
    #                                     "avaaaaaaaa", "bvaaaaaaaa", "cvaaaaaaaa", "dvaaaaaaaa", "evaaaaaaaa", "fvaaaaaaaa", "gvaaaaaaaa",
    #                                     "hvaaaaaaaa", "ivaaaaaaaa", "jvaaaaaaaa", "kvaaaaaaaa", "lvaaaaaaaa", "mvaaaaaaaa", "nvaaaaaaaa",
    #                                     "ovaaaaaaaa", "pvaaaaaaaa", "qvaaaaaaaa", "rvaaaaaaaa", "svaaaaaaaa", "tvaaaaaaaa", "uvaaaaaaaa",
    #                                     "vvaaaaaaaa", "wvaaaaaaaa", "xvaaaaaaaa", "yvaaaaaaaa", "zvaaaaaaaa", "awaaaaaaaa", "bwaaaaaaaa",
    #                                     "cwaaaaaaaa", "dwaaaaaaaa", "ewaaaaaaaa", "fwaaaaaaaa", "gwaaaaaaaa", "hwaaaaaaaa", "iwaaaaaaaa",
    #                                     "jwaaaaaaaa", "kwaaaaaaaa", "lwaaaaaaaa", "mwaaaaaaaa", "nwaaaaaaaa", "owaaaaaaaa", "pwaaaaaaaa",
    #                                     "qwaaaaaaaa", "rwaaaaaaaa", "swaaaaaaaa", "twaaaaaaaa", "uwaaaaaaaa", "vwaaaaaaaa", "wwaaaaaaaa",
    #                                     "xwaaaaaaaa", "ywaaaaaaaa", "zwaaaaaaaa", "axaaaaaaaa", "bxaaaaaaaa", "cxaaaaaaaa", "dxaaaaaaaa",
    #                                     "exaaaaaaaa", "fxaaaaaaaa", "gxaaaaaaaa", "hxaaaaaaaa", "ixaaaaaaaa", "jxaaaaaaaa", "kxaaaaaaaa",
    #                                     "lxaaaaaaaa", "mxaaaaaaaa", "nxaaaaaaaa", "oxaaaaaaaa", "pxaaaaaaaa", "qxaaaaaaaa", "rxaaaaaaaa",
    #                                     "sxaaaaaaaa", "txaaaaaaaa", "uxaaaaaaaa", "vxaaaaaaaa", "wxaaaaaaaa", "xxaaaaaaaa", "yxaaaaaaaa",
    #                                     "zxaaaaaaaa", "ayaaaaaaaa", "byaaaaaaaa", "cyaaaaaaaa", "dyaaaaaaaa", "eyaaaaaaaa", "fyaaaaaaaa",
    #                                     "gyaaaaaaaa", "hyaaaaaaaa", "iyaaaaaaaa", "jyaaaaaaaa", "kyaaaaaaaa", "lyaaaaaaaa", "myaaaaaaaa",
    #                                     "nyaaaaaaaa", "oyaaaaaaaa", "pyaaaaaaaa", "qyaaaaaaaa", "ryaaaaaaaa", "syaaaaaaaa", "tyaaaaaaaa",
    #                                     "uyaaaaaaaa", "vyaaaaaaaa", "wyaaaaaaaa", "xyaaaaaaaa", "yyaaaaaaaa", "zyaaaaaaaa", "azaaaaaaaa",
    #                                     "bzaaaaaaaa", "czaaaaaaaa", "dzaaaaaaaa", "ezaaaaaaaa", "fzaaaaaaaa", "gzaaaaaaaa", "hzaaaaaaaa",
    #                                     "izaaaaaaaa", "jzaaaaaaaa", "kzaaaaaaaa", "lzaaaaaaaa", "mzaaaaaaaa", "nzaaaaaaaa", "ozaaaaaaaa",
    #                                     "pzaaaaaaaa", "qzaaaaaaaa", "rzaaaaaaaa", "szaaaaaaaa", "tzaaaaaaaa", "uzaaaaaaaa", "vzaaaaaaaa",
    #                                     "wzaaaaaaaa", "xzaaaaaaaa", "yzaaaaaaaa", "zzaaaaaaaa"]))
# tool.print_matrix(input3)
