import sys




def main():
    print("当ファイルの実行に成功")
    # 数字を受け取る
    K = int(input())

    #　配列として受け取る（スペースで区切って入力すること）
    A, B = map(int, input().split())
    print(A,B)

    exist = False

    for i in range(A, B + 1):
        if i % K == 0:
            print("in")
            exist == True

    # print("OK" if exist == True else "NG")
    print(exist)

    if exist:
        print("ok")
    else:
        print("ng")






if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        sys.exit()