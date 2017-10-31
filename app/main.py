import random


def is_prime(q, k=50):
    # 素数の判定用関数
    # ミラー・ラビンテストを用いる
    q = abs(q)
    if q == 2:
        return True
    if q < 2 or q & 1 == 0:
        return False

    d = (q-1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1, q-1)
        t = d
        y = pow(a, t, q)
        while t != q-1 and y != 1 and y != q-1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q-1 and t & 1 == 0:
            return False
    return True


def gcd(a, b):
    # aとbが互いに素であるか確かめる
    if a > b:
        while b > 0:
            a, b = b, a % b
        return a
    else:
        while a > 0:
            b, a = a, b % a
        return b


def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    # まず，入力の違反確認
    if len(argv) != 3:
        print(-1)
        return 0
    for i, v in enumerate(argv):
        if v.isdigit() is False:
            print(-1)
            return 0
    # 入力値を変数に代入
    a = int(argv[0])
    b = int(argv[1])
    m = int(argv[2])
    if gcd(a, b) != 1:
        print(-1)
        return 0
    i = 0
    n = 1
    num = 0
    # n=1から順に計算し，素数かどうか確認
    # 素数の数がmに一致するまで行う
    while(i < m):
        num = a * n + b
        if is_prime(num) is True:
            i += 1
        n += 1
    print(num)


if __name__ == "__main__":
    main(["29", "47", "239"])
