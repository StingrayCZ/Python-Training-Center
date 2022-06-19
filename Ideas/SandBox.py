import math

# @Aplikace_prodf
# def test():
#     pass

# for _ in range(len(dir(math))):
#     print(dir(math)[_])


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")