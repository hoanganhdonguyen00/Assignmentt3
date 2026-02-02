numbers = []

while True:
    s = input("Mỗi lần nhập 1 số (empty to quit): ")

    if s == "":
        break

    numbers.append(float(s))

if numbers:
    print("Smallest:", min(numbers))
    print("Largest:", max(numbers))
