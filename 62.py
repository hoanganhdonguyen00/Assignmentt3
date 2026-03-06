while True:
    month_input = input("Nhập số tháng: ")
    if month_input == "":
        print("Thoát...")
        break
    try:
        month = int(month_input)
        if 1 <= month <= 3:
            season = "Spring"  
        elif 4 <= month <= 6:
            season = "Summer"   
        elif 7 <= month <= 9:
            season = "Autumn"   
        elif 10 <= month <= 12:
            season = "Winter"   
        else:
            print("Xin mời nhập lại.")
            continue
        print(f"Month {month} is in {season}.")
    except ValueError:
        print("Lại.")