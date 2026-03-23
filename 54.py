number = []
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
ThamSo = [1, 2, 4, 5, 3, 9, 7]
result = sum_list(ThamSo)

print("Tổng:", result)