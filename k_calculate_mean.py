values = [10, 20, 30, 40, 50]

def calculate_mean(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

print(calculate_mean(values))
values = []
print(calculate_mean(values))