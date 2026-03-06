names = set()

while True:
    name = input("Nhập tên: ")
    if name == "":
        break
    if name in names:
        print("Tên hiện có")
    else:
        print("Tên mới")
        names.add(name)

print("\nTất cả:")
for n in names:
    print(n)