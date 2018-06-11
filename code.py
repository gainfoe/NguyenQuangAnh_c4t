while True:
    while True:
        try:
            size = int(input("Nhap co chu: "))
            if size < 1:
                print("Nhap so nguyen duong di dmm")
            else:
                break
        except ValueError:
            print("Nhap so nguyen duong di dmm")

    for i in range(size):
        if i == 0 or i == size - 1:
            for j in range(4):
                if j == 2:
                    print("* " * (size - 1), end="")
                    print("  ", end="")
                else:
                    print("* " * size, end="")
                print("\t", end="")
            print()
        else:
            for j in range(4):
                if j == 0 or j == 3:
                    print("* ", end="")
                    if j == 3 and i == int((size - 1) / 2):
                        print("* " * (size - 1), end="")
                    else:
                        print("  " * (size - 1), end="")
                else:
                    print("* ", end="")
                    print("  " * (size - 2), end="")
                    print("* ", end="")
                print("\t", end="")
            print()
    while True:
        action = input("Continue / Stop: ").lower()
        if action == "continue" or action == "stop":
            break

    if action == "stop":
        break















