a = int(input())
i=0
while True:
    i+=1
    if int((a+i)**0.5)**2==a+i:
        print(a+i)
        break
    elif int((a+i)**0.5)**2==a+i:
        print(a-i)
        break