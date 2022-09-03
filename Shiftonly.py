import sys




def main():
    print("tesuto")
    N = int(input())
    A = list(map(int, input().split()))
    print(N,A)


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        sys.exit()