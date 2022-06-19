#
# # Python program to demonstrate working
# # of map.
#
# # Return double of n
# def addition(n):
# 	return n + 5
#
# # We double all numbers using map()
# numbers = (1, 2, 3, 4, 5)
# result = map(addition, numbers)
# print(result)
# print(list(result))
# print(tuple(result))
#
#


def test(funkcia):
	funkcia()
	print("JJ")
	funkcia()

@test
def percentage():
	print("%"*30)




print(test)