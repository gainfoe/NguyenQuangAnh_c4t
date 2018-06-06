#In 20 so 1 va 0 lien tiep

list = [1, 0]
print(*(list * 10))

#In n so 1 va 0 lien tiep

so_nhap = None

while so_nhap is None:
    try:
        so_nhap = int(input("Nhap tong so luong so 1 va 0: "))
        if so_nhap < 1:
            print("Khong phai so nguyen duong")
            so_nhap = None
    except ValueError:
        print("Loi cu phap")

for i in range(1, so_nhap + 1):
    if i % 2 == 1:
        print(1, end=" ")
    else:
        print(0, end=" ")
