n = 5
# print(("*"*n + "\n")*n)
#
# for i in range(1, n+1):
#     print("*"*i)
#
# for i in range(1, n + 1):
#     print((n-i)*" " + (i*"*"))

# for i in range(1, n + 1):
#     if i % 2 != 0:
#         print(((n - i) // 2)*" " + i*"*" + ((n - i) // 2)*" ")

for i in range(1, n+1, 2):
    print(("*"*i).center(n))