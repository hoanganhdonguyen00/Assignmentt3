number = []
num = int(input("Nhập số: "))
if num < 2:
    print("Không phải là số nguyên số")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Là số nguyên tố")
    else:
        print("Không phải là số nguyên tố")