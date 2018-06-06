so_nhap = None

while so_nhap is None:
    try:
        so_nhap = int(input("Nhap so nguyen duong: "))
        if so_nhap < 1:
            print("Khong phai so nguyen duong")
            so_nhap = None
    except ValueError:
        print("Loi cu phap")

fac = 1

for i in range(so_nhap):
    fac = fac * (i + 1)

print("Giai thua la:", fac)


