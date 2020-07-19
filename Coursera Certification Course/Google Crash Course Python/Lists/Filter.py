# # Create a list of strings: fellowship
# fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
#
# # Use filter() to apply a lambda function over fellowship: result
# result = (lambda member: len(member) > 6, fellowship)
#
# # Convert result to a list: result_list
# result_list = list(result)
#
# # Print result_list
# print(result_list)
#
# # using Function work on Filter

# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def evenNumber(num):
#     return num % 2 == 0
#
#
# evens = filter(evenNumber, myList)
# print(list(evens))
#
# # We can try to using Lambda Function
# evenss = filter(lambda num: num % 2 == 0, myList)
#
# print(list(evenss))

