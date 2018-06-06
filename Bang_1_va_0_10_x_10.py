for i in range(1, 11):
    for j in range(1,11):
        if (i + j) % 2 == 0:
            print(1, end="\t")
        else:
            print(0, end="\t")
    print("\n")
