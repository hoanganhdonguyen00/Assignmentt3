while True:
    inch = float(input("Enter inches (no negative number pls): "))

    if inch < 0:
        print("end")
        break

    cm = inch * 2.54
    print(inch, "inches =", cm, "cm")
