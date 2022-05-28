import math


bin_number = []
TEST = True
i = 1
while TEST:

    test_number = str(input("Enter binary number"))

    for _ in test_number:
        print("Test")
        if int(_) != 0 and int(_) != 1:
            print(f"cislo {_} neni 0 a ani 1")
            print(type(_))
            TEST = True
        else:
            TEST = False


print(test_number)

# print(len(test_number))

for _ in range(len(test_number)):
    if int(_)%2 == 0:



# print(29 % 2)

def DecToBin(num):
    pass


def ProofBin():
    pass