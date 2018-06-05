from random import *

list_word = ["champion", "love", "heart", "hexagon", "cute"]
end = 5
while end != 0:
    char = []
    random_number = randint(0, len(list_word) - 1)
    word = list_word[random_number]
    list_word.pop(random_number)
    char_list = []
    do_dai = len(word)
    end = end - 1

    for i in range(do_dai):
        a = word[i]
        char_list.append(a)
    for _ in range(do_dai):
        thu_tu = randint(0, len(char_list) - 1)
        chu = char_list[thu_tu]
        char.append(chu)
        char_list.pop(thu_tu)

    print(*char, sep=" ")

    while True:
        doan = input("Nhap tu: ")
        if doan.lower() == word:
            print("Chinh Xac")
            break
        print("Khong Chinh Xac")

    if end != 0:
        while True:
            action = input("Next / Stop: ")
            if action.lower() == "next":
                print("Cau tiep theo:")
                break
            elif action.lower() == "stop":
                end = 0
                print("Tro choi ket thuc")
                break
            else:
                print("Loi cu phap")
    else:
        print("Ban da chien thang")











