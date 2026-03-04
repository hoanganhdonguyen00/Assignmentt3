import re

def sum_numbers_in_text(text):
    numbers = re.findall(r'\d+', text)
    total = 0

    for n in numbers:
        total += int(n)

    return total
text = "Today is March 4, 2026. The temp is about 30 degrees."
print(sum_numbers_in_text(text))