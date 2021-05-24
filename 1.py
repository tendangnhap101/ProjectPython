c = input("Văn bản cần xử lý: ")
for i in range(0,8):
    print("1 \n 2 \n 3 \n 4 \n 5 \n")
    x = int(input('Chọn số: '))
    a = b = ''
    if (x==1):
        a = input('Nhập từ cần thay thế: ')
        b = input('Nhập từ thay thế: ')
        NewString = c.replace(a,b)
        print(NewString)
    elif ( x== 2):
        print(c.upper())
    elif(x==3):
        print(c.lower())
    elif(x==4):
        print(c.capitalize())
    elif(x==5):
        print(c.split())
