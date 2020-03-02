'''Driver to the Test github program'''


def foo():
    print("hello, foo")


def hello_world():
    foo()
    print('hello world')

def print_nums():
    for i in range(5):
        print(i)

if __name__ == '__main__':
    hello_world()
    print_nums()