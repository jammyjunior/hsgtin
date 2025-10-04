a = int(input())
for i in range(1, a+1):
    j=i+1
    if i*j == a:
        print(i, j)
        break
else:
    print("khong")