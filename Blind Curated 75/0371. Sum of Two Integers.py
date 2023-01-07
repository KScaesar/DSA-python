class Solution:
    # https://leetcode.com/problems/sum-of-two-integers/
    def getSum(self, a: int, b: int) -> int:
        # 一開始看不懂 題目想要求什麼實做
        # 查資料才發現, 是跟 位元操作有關聯
        #
        # https://github.com/apachecn/apachecn-algo-zh/blob/master/docs/leetcode/python/371._sum_of_two_integers.md
        # https://ithelp.ithome.com.tw/articles/10300637
        # 对x和y来做加法
        # 末位会是x XOR y，进位会是x AND y
        #
        # 分為兩個部份
        # 1. 下一個位元的進位
        # 2. 這個位元的和除了進位之外的和
        #
        # 加減乘除
        # 進位:carry 借位:borrow
        #
        # simple Half Adder logic that can be used to add 2 single bits
        # 邏輯電路設計
        # 加法器 是所有運算的根本
        # http://ocw.ksu.edu.tw/file.php/6/%E6%95%99%E6%9D%90%E6%8A%95%E5%BD%B1%E7%89%87%EF%BC%88pdf%EF%BC%89/%E7%AC%AC%E4%BA%94%E7%AB%A0.pdf

        # 1 byte = 8 bit = 0xFF = 0b11111111 = 256
        # 32 位元系統中的整數使用二進位表示，並且有 32 個位置供儲存資料。
        # 最高位（第 32 位）用來儲存正負號，
        # 0 表示正數，1 表示負數。
        # 因此，在 32 位元系統中，
        # 最大的正整數是 0111 1111 1111 1111 1111 1111 1111 1111 = 0x7FFFFFFF
        # 最大的負整數是 1111 1111 1111 1111 1111 1111 1111 1111 = 0x80000000
        #
        # https://ithelp.ithome.com.tw/articles/10273162
        # https://blog.csdn.net/dovakejin/article/details/112446946
        # 最大值：符号位置为0后，还剩下31位，这31位可以组成的二进制数的个数为2 ^ 31 = 2,147,483,648。
        # 由于000 0000 0000 0000 0000 0000 0000 0000这种情况需要用来表示数值0，所以还剩下2,147,483,647
        # 最小值：同样的，符号位置为1后，还剩下31位，可以表示2,147,483,648个数，因为在负数是以补码形式存储的，
        # -0和0的补码是一样的。为了不造成资源的浪费，
        # 将 1000 0000 0000 0000 0000 0000 0000 0000这个二进制数用来表示-2,147,483,648

        # 由於 python 沒有型別, a 或 b 是 負號的情況, 需要特別處理
        # python 非常適合處理超過最大長度的大整數, 可以處理任意長度的整數。
        # 但如果我們不在最大長度處停止，那也會造成無限循環。
        # https://leetcode.com/problems/sum-of-two-integers/solutions/84282/python-solution-with-no-completely-bit-manipulation-guaranteed/?orderBy=most_votes

        # Python 的整數沒有限制, 端看你電腦的記憶體有多大, Python 的整數是採用 2 的補數來表示
        # https://dev.to/codemee/python-de-wei-yuan-yun-suan-5bgb

        # 補數計算機
        # https://begoodtool.com/binary

        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF

        next_carry = 0
        carry = ((a & b) << 1) & mask
        _sum = (a ^ b) & mask

        # print(f'a={bin2(a & mask)} b={bin2(b & mask)}')
        # print(len(bin2(a ^ b)) - 2, bin2(a ^ b), a ^ b)
        # print(len(bin(a ^ b)) - 2, bin(a ^ b), a ^ b)
        # print()
        #
        # print(len(bin2(_sum)) - 2, bin2(_sum), _sum)
        # print(len(bin(_sum)) - 2, bin(_sum), _sum)
        # print()

        while carry:
            next_carry = (carry & _sum) << 1
            next_carry &= mask

            _sum = (carry ^ _sum)
            _sum &= mask

            carry = next_carry

        print(f'bit={len(bin2(_sum)) - 2} {bin2(_sum)}, bit={len(bin(_sum)) - 2} {bin(_sum)}')
        print(f'bit={len(bin2(~(_sum ^ mask))) - 2} {bin2(~(_sum ^ mask))}, bit={len(bin(~(_sum ^ mask))) - 2} {bin(~(_sum ^ mask))}')

        # (_sum ^ mask) 可以看成 進行 低位元32bit 的 not 運算
        # 由於要恢復成原本的數值
        # 所以要進行第二次 not, 這次使用普通的 ~
        # 對所有位元進行 not 運算
        #
        # 第一次只對 低位 32bit 進行 not
        # 第二次 對 所有位元進行 not
        return _sum if _sum <= MAX else ~(_sum ^ mask)
        # return _sum if _sum <= MAX else (_sum | ~mask) # 寫法 2 看不懂


def bin2(num):
    # https://dev.to/codemee/python-de-wei-yuan-yun-suan-5bgb
    # https://stackoverflow.com/questions/46573219/the-meaning-of-bit-wise-not-in-python
    # std bin() 不會顯示符號位元, 只會顯示數字位元的部份
    # 當遇到負號時, 前綴加上 '-'符號, 數字位元維持正數的二進位格式
    #
    # 此函數會顯示符號位元, 且 數字位元 以二補數的格式 顯示

    bits = num.bit_length() + 1  # 計算位元數, +1 是為了計算符號的位元
    mask = (1 << bits) - 1  # 相同位元數全為 1 的數
    num_bin2 = mask & num

    if num < 0:
        # +2 是把 0b 兩個前綴符號算進去?
        return f"{num_bin2:#{bits + 2}b}"  # 2 進位表示
    else:
        return f"{num_bin2:#0{bits + 2}b}"  # 正數補上正負號位元


def test():
    n = -5
    mask = (1 << n.bit_length() + 1) - 1
    # mask = 0xFFFFFFFF

    print(f'{bin2(n)}', n)
    print(f'{bin(n)}', n)
    print()

    print(f'{bin2(~n)}', ~n)
    print(f'{bin(~n)}', ~n)
    print()

    print(f'{bin2(n ^ mask)}')
    print(f'{bin(n ^ mask)}')
    print()

    print(f'{bin2(n & mask)}')
    print(f'{bin(n & mask)}')
    print()

    # print(f'{bin2(n)}', n)
    # print(f'{bin2(n & mask)}')


if __name__ == '__main__':
    # print(Solution().getSum(2, 3))
    print(Solution().getSum(-3, 1))
    print()

    # test()
