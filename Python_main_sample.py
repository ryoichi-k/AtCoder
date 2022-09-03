import sys




def main():
    # 数字を受け取る
    N = int(input())

    #　配列として受け取る（スペースで区切って入力すること）
    A = list(map(int, input().split()))
    print(N,A)



if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        sys.exit()