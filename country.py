import sys


def main():
    print("hello world")
    print("goodbye")

    if(sys.argv[1] == 'france'):
        print("i am from France")

    else:
        print("Second col.")


if __name__ == "__main__":
    main()
