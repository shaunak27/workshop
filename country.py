import sys


def main():
    print("hello world")
    print("goodbye")

    if(sys.argv[1] == 'france'):
        print("i am from France")

    else(sys.argv[1] == 'india'):
        print("I am from India")


if __name__ == "__main__":
    main()
