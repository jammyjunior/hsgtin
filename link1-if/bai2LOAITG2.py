a, b, c = map(int, input().split())
check = a+b>c and a+c>b and b+c>a
if a==b==c:
    print("Tam giac deu")
elif (a==b or b==c or a==c) and check == True:
    print("Tam giac can")
elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("Tam giac vuong")
elif check == True:
    print("Tam giac thuong")
else:
    print("Khang la tam giac")