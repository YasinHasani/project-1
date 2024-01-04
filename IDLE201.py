n = int(input("عدد خود را وارد کنيد ="))

for i in range(n):
    for j in range(i):
        print(i,end='  ')
    print()
