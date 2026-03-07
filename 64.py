def word_frequency(text):
    frequency = {}
    words = text.split()
    for word in words:
        word = word.lower()  
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
Nhập = "1, 3, 2, 5, 6, hello hi my name hi hoang anh ."
print(word_frequency(Nhập))