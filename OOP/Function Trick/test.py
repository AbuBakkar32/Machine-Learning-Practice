# def bswitch(b):
#     return bswitch._system_dic.get(b, "Sorry, i didn't get anything")
#
#
# bswitch._system_dic = {'mango': 5, 'apples': 7, 'orange': 8, 'green': 9, 'purple': 10}
# print(bswitch())


x = list(filter(lambda x: all(x % y != 0 for y in range(2, x)), range(2, 13)))
print(x)
