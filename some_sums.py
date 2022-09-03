import sys

# 1以上N以下の整数のうち
# 十進数での各桁の和がA以上B以下であるものの総和を求める

# 整数nの格桁の和を求める
def calc(n):
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n //= 10
    return sum_digit


def main():
    print("当ファイルの実行に成功")
    # 数字を受け取る
    # N = int(input())

    # #　配列として受け取る（スペースで区切って入力すること）
    # A = list(map(int, input().split()))
    # print(N,A)

    N, A, B = map(int, input().split())

    result = 0

    for i in range(1, N+1):
        if A <= calc(i) <= B:
            result += i
    print("result")
    print(result)




if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        sys.exit()