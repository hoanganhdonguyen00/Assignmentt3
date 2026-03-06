numbers = []

while True:
    num = input("Hãy nhập số: ")
    if num == "":
        break
    try:
        numbers.append(float(num))
    except ValueError:
        print("Chọn lại số phù hợp.")

#numbers.sort(reverse=True)
#top5 = numbers[:5]

print("các số được sắp xếp theo thứ tự là:", top5)