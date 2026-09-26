text = "aaabbccccdaa"
# text = "aabbbcccdddddeeeaaaabbbb"

def run_length_encode(text):
    alphabets_count = ""
    current = text[0]
    count = 0
    
    for i in text:
        if i == current:
            count = count + 1            
        else:
            alphabets_count += f"{current}{count}"
            current = i
            count = 1
    
    alphabets_count += f"{current}{count}"
    
    return alphabets_count

print(run_length_encode(text))
            