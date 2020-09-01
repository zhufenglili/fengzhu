li=[22,33,4,4,4,55,5,88,99]
lii = []
# for i in li:
#     if i not in lii:
#         lii.append(i)
#         if i == 88:
#             lii.remove(88)
#         elif i == 99:
#             lii.remove(99)
# print(lii)
for i in li:
    lii.append(i)
    if i == 88:
        lii.remove(88)
a=set(lii)
print(a)