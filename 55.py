number = []
def remove_odd(numbers):
    even_list = []
    
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    
    return even_list
EX = [1, 2, 3, 4, 5, 6, 7, 8]

SoChan = remove_odd(EX)

print("EX:", EX)
print("Số chẵn:", SoChan)