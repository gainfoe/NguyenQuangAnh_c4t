intro_1 = "Our item: "
intro_2 = "Our items: "
item = ["T-Shirt", "Sweater"]
while True:
    action = input("Wecome to our shop. What do you want: (C, R, U, D) or Stop ? ")
    action_low = action.lower()
    intro = intro_2
    if action_low == "c":
        new_item = input("Enter new item: ")
        item.append(new_item)
        if len(item) != 1:
            intro = intro_2
        print(intro, end="")
        print(*item, sep=", ")
    elif action_low == "r":
        print(intro, end="")
        print(*item, sep=", ")
    elif action_low == "u":
        posi = int(input("Update position: "))
        if posi > len(item):
            print("Khong ton tai")
        else:
            new_item = input("Enter new item: ")
            item[posi - 1] = new_item
            print(intro, end="")
            print(*item, sep=", ")
    elif action_low == "d":
        posi = int(input("Delete position: "))
        if posi > len(item):
            print("Khong ton tai")
        else:
            item.pop(posi - 1)
            if len(item) == 1:
                intro = intro_1
            print(intro, end="")
            print(*item, sep=", ")
    elif action_low == "stop":
        print("Tam dung")
        khoi_dong = input("Nhap Start de bat dau, End de ket thuc: ")
        if khoi_dong.lower() == "start":
            pass
        elif khoi_dong.lower() == "end":
            break
        else:
            print("Loi cu phap")
    else:
        print("Loi cu phap")
print("Ket thuc")




