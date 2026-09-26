values = [1, 2, 3, 9, 4, 6, 7, 4]

def calculate_median(numbers):
    numbers = sorted(numbers)
    mid = len(numbers) // 2
    
    if len(numbers) % 2 == 1:
        return numbers[mid]
    else:
        return int((numbers[mid - 1] + numbers[mid]) / 2)
    
print(calculate_median(values))