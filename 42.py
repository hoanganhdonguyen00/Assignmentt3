import re

def color(color):
    pattern = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(pattern, color))
print(color("#04FF00"))
print(color("#ff23ed"))   
print(color("#GGG9GG"))   