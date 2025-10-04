a = float(input())
if a<=1:
    print(5000)
elif a<=5:
    print(f"{5000+(a-1)*4500:.2f}")
elif a<=120:
    print(f"{5000+4*4500+(a-5)*3500:.2f}")
else:
    print(f"{(5000+4*4500+(a-5)*3500)*0.9:.2f}")