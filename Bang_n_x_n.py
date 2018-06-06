so_nhap = None

while so_nhap is None:
    try:
        so_nhap = int(input("Nhap so nguyen duong: "))
        if so_nhap < 1:
            print("Khong phai so nguyen duong")
            so_nhap = None
    except ValueError:
        print("Loi cu phap")

for i in range(1, so_nhap + 1):
    for j in range(1, so_nhap +1):
        print(j * i, end="\t")
    print("\n")