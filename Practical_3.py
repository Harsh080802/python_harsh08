""" Student ID: 20CS050
    Student Name : HARSH PATEL 
"""
x = input()
roomlist = input().split()
roomset = set(roomlist)

for y in list(roomset):
    roomlist.remove(y)

CAP_RO_NUM = roomset.difference(set(roomlist)).pop()
print(CAP_RO_NUM)
