a = int(input())
sum=0
i=0
while True:
    i+=1
    sum+=i
    if sum == a:
        print(i)
        break
    elif sum>a:
        print("khong")
        break