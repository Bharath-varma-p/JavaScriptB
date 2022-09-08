# N = int(input("N="))
# print(N)
# a = []
# for i in range(N):
#     x = int(input("Enter the array element "))
#     a.append(x)

# print(a)

# beautiful = []
# if len(a) != 0:
#     beautiful.append(a[0])
# print(beautiful)


from pickle import TRUE


a = [4, 2, 1, 3]
print(a)
beauty = []

len = len(a)

# print(sum(a))
b = a.sort()
print(a)
beauty = []
beauty.append(a[0])
count = 0
i = 1
N = 4
# l = len(a)
b.pop(a[0])
for x in range(4):
    if sum(a[:i]) <= a[i]:
        print(a[:i], a[i])
        count += 1
        print(count)
        i += 1

print(count)
