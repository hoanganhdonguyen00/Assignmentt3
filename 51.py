numbers = []
while True:
    user_input = input("Nhập số, để trống để tắt: ")
    
    if user_input == "":
        break
    numbers.append(float(user_input))
numbers.sort(reverse=True)
highest = numbers[:5]

print("5 số lớn nhất", highest)