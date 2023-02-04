# 杰悉科技 leetcode 測驗 2023-02-02


# You are tasked with splitting the 7th grade class into two teams for a soccer game.
# Given a list of students and their "enemies" aka the kids they can't be on th same team as,
# determine whether it is possible to split the class in two in such a way that no child is on the same
# team as any of their enemies. if possible, return the two teams.
#
# David: [Lucy, Jose, Chris]
# Lucy: [David, Brian, Emily]
# Emily: [Lucy, Jack]
# Jose: [David, Paul]
# Paul: [Jose, Chris]
# Chris: [Paul, David, Brian]
# Brian: [Lucy, Chris, Jack]
# Jack: [Brian, Emily]

# https://half-daphne-1c8.notion.site/NADI-Interview-Coding-Test-635-a853799705e1401f9aa84f42dd5d2ee2

def code1_v2(st: dict[str, list[str]]):
    # 有一方堅決不想跟對方交往 那就不會交往 的意思
    # 不用雙方都不想跟對方交往
    #
    # 只要有一邊不行 他們就不會同隊
    #
    # 不能只是照著字面的意思
    # 依照討厭的人 畫graph
    #
    # 現在只在意誰跟誰, 不能一個隊伍
    # 誰跟誰不能一隊 這個東西 沒有方向性

    # 應該把 graph 思考為
    # edge 頂點兩端，不是同一個隊伍
    # 這樣就是 無向圖
    #
    # 我之前定義 的 edge 是
    # 是否討厭對方, 是有方向性的

    # bipartite graph

    def dfs(graph, cursor, color, memo):
        nonlocal can_game
        if cursor in memo or not can_game:
            return

        memo[cursor] = color

        for _next in graph[cursor]:
            if memo.get(_next, 0) != 0 and memo[_next] == memo[cursor]:
                can_game = False
                return
            dfs(graph, _next, -color, memo)

    memo = dict()
    can_game = True
    color = 1
    for person in st.keys():
        dfs(st, person, color, memo)

    if can_game:
        team1 = [k for k, v in memo.items() if v > 0]
        team2 = [k for k, v in memo.items() if v < 0]
        print(f'team1={team1}')
        print(f'team2={team2}')
    else:
        print("no game")


def code1_v1(st: dict[str, list[str]]):
    team1 = set()
    team2 = set()
    can_game = True

    def dfs(st, cursor, kind: int, visited):
        nonlocal can_game
        if not can_game:
            return

        if cursor not in visited:
            visited.add(cursor)
        else:
            return

        if kind > 0:
            # 敵人 的 敵人, 不一定是朋友
            # 可能是我的敵人, 所以要進行判斷

            # 兩個方向 都要判斷
            # 單純判斷 某一個方向, 在某些情況會判斷錯誤

            # 已入隊伍的人 是否 討厭 將要入隊伍的人
            for user in team1:
                if cursor in st[user]:
                    can_game = False
                    return

            # 將要入隊伍的人 是否 討厭 已入隊伍的人
            for user in st[cursor]:
                if user in team1:
                    can_game = False
                    return

            team1.add(cursor)
        else:
            for user in team2:
                if cursor in st[user]:
                    can_game = False
                    return

            for user in st[cursor]:
                if user in team2:
                    can_game = False
                    return

            team2.add(cursor)

        for v in st[cursor]:
            dfs(st, v, -kind, visited)

    visited = set()
    for key in st.keys():
        dfs(st, key, 1, visited)

    if can_game:
        print(f'team1={team1}')
        print(f'team2={team2}')
    else:
        print("no game")


if __name__ == '__main__':
    st = {
        "David": ["Lucy", "Jose", "Chris", ],
        "Lucy": ["David", "Brian", "Emily"],
        "Emily": ["Lucy", "Jack"],
        "Jose": ["David", "Paul"],
        "Paul": ["Jose", "Chris", ],
        "Chris": ["Paul", "David", "Brian"],
        "Brian": ["Lucy", "Chris", "Jack"],
        "Jack": ["Brian", "Emily"],
    }
    code1_v1(st)
    print()
    code1_v2(st)
