import sys




def main():
    print("tesuto")
    N = int(input())
    A = list(map(int, input().split()))
    print(N,A)

    # 操作回数
    count = 0

    while True:
        can_do = True
        for i in range(N):
            if A[i] % 2 == 1:
                can_do = False

        if not can_do:
            break

        for i in range(N):
            A[i] //= 2

        count += 1

    print(count)


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        sys.exit()