a, b, x, y = map(int, input().split())
if (a%2==0 and b%2==0 and x%2==0 and y%2==0) or (a%2==1 and b%2==1 and x%2==1 and y%2==1):
    print("Trung mau")
else:
    print("Khong trung mau")