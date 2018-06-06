#In 20 so bat dau tu 0

print(*range(20))

#In n so bat dau tu 0

so_nhap = None

while so_nhap is None:
    try:
        so_nhap = int(input("Nhap so nguyen duong: "))
        if so_nhap < 1:
            print("Khong phai so nguyen duong")
            so_nhap = None
    except ValueError:
        print("Loi cu phap")

print(*range(so_nhap))







