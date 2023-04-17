# a = input().split()
# for i in a:
#     if "@" in i:
#         print(i)
#         break

# print([i for i in input().split() if "@" in i][0])

a = input()

em1 = a.index("@")
em2 = a.rindex(" ", 0, em1)
em3 = a.index(" ", em1, len(a))
em = a[em2 + 1 : em3 + 1]

print(em)
