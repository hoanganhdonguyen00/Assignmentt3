cities = []

for i in range(5):
    name = input(f"Nhập thành phố: ")
    
    if name == "":
        break
    cities.append(name)
print("Thành phố:")
for city in cities:
    print(city)