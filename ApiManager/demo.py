#! /usr/bin/env python
# -*- coding:utf-8 -*-


# import heapq
#
# nums = [1, 3, 5, 6, 9, 3, 12, 89, 96, 128, 33, 65]
#
#
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))
#
#
# from collections import Counter
#
# words = [
#     "look", 'into', 'my', 'eyes', 'look', 'my', "look", 'into', 'my', 'eyes', 'look', 'my',
#     "look", 'into', 'my', 'eyes', 'look', 'my', 'into', 'under', 'up', 'i', 'do not'
# ]
#
#
# count = Counter(words)
# print(count)

# from operator import itemgetter
#
# rows = [
#     {'fname': "john", 'lname': 'Clease', 'uid': 1003},
#     {'fname': "David", 'lname': 'jones', 'uid': 1002},
#     {'fname': "Big", 'lname': 'jones', 'uid': 1001},
#     {'fname': "Brian", 'lname': 'Bean', 'uid': 1004},
# ]
#
# row_by_fname = sorted(rows, key=itemgetter("fname"))
#
# print(sorted(rows, key=lambda i: i["fname"]))

# from itertools import groupby
#
# rows = [
#     {'address': "5123 N Shanghai",  'date': '07/03/2017'},
#     {'address': "5531 N Beijing",  'date': '06/02/2016'},
#     {'address': "4562 W Gansu",  'date': '07/03/2017'},
#     {'address': "3512 C Hebei",  'date': '09/23/2018'},
#     {'address': "6421 S Shenzhen",  'date': '09/22/2015'},
# ]
#
# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print(" ", i)
#


from collections import ChainMap

# a = {'x': 1, 'z': 3}
# b = {'y': 9, 'z': 6}

# c = ChainMap(a, b)
# print(c)
#
# print(c['x'])


