import re

def is_valid_course_code(code):
    pattern = r'^[A-Z]{3}[0-9]{3}$'
    return bool(re.match(pattern, code))

print(is_valid_course_code("TEC999"))   
print(is_valid_course_code("ABc123"))   
print(is_valid_course_code("A1C333"))   