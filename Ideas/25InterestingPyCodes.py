# # create a nested list
# nlist1 = [[]]
# nlist2 = [[1,2],[3,4,5]]
#
# # create a list with list comprehension
# nlist_comp1 = [[i for i in range(5)], [i for i in range(7)], [i for i in range(3)]]
# nlist_comp2 = [[i for i in range(n)] for n in range(3)]
# print(nlist_comp1)
# print(nlist_comp2)
#
# # [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2]]
# # [[], [0], [0, 1]]
#
#
# # print(i for i in range(5))
# listtest = []
# listtest = [[i for i in range(10)]]
# print(listtest)

odds = [1,3,5,7,9]
evens = [2,4,6,8,10]
fevens = [2,4,6,8,10]
for oddnum, evennum, bb in zip(odds,evens, fevens):
    print(oddnum + evennum + bb)
    # print(evennum)