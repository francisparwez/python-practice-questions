text = "data science is about data"

frequency = {}

for char in text:
    if char == ' ':
        continue
    frequency[char] = frequency.get(char, 0) + 1
    
print(frequency)