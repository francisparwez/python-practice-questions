numbers = [4, 7, 2, 4, 9, 7, 1, 2, 8, 4]

occurrence = {num: numbers.count(num) for num in set(numbers) if numbers.count(num) > 1}

print(occurrence)