def permutation3(nums: list[int]) -> list[list[int]]:
    def backtrack(nums, track, used):
        nonlocal ans
        if len(track) == size:
            ans.append(track.copy())
            return

        for i in range(size):
            if i in used:
                continue

            used.add(i)
            v = nums[i]
            track.append(v)
            backtrack(nums, track, used)
            track.pop()
            used.remove(i)

    size = len(nums)
    ans = []
    backtrack(nums, [], set())
    return ans


def permutation2(nums: list[int]) -> list[list[int]]:
    def backtrack(nums: list[int], track: list[int]):
        nonlocal ans

        if len(track) == len(nums):
            ans.append(track.copy())
            return

        for i in range(len(nums)):
            v = nums[i]

            # 把不合法元素排除
            if track.count(v) != 0:
                continue

            track.append(v)
            backtrack(nums, track)
            track.pop()

    ans = []
    backtrack(nums, [])
    return ans


def permutation1(nums: list[int]) -> list[list[int]]:
    def backtrack(nums: list[int], track: list[int]):
        nonlocal result

        if len(nums) == 0:
            result.append(track.copy())
            return

        for i in range(len(nums)):
            v = nums.pop(i)

            track.append(v)
            backtrack(nums, track)
            track.pop()

            nums.insert(i, v)

    result = []
    backtrack(nums, [])
    return result


if __name__ == '__main__':
    print(permutation1([1, 2, 3]))
    print(permutation2([1, 2, 3]))
    print(permutation3([1, 2, 3]))
