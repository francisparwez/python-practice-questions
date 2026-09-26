# Example with multiple missing numbers: 4 and 7 are missing
numbers = [1, 2, 3, 4, 5, 8, 9]

expected_num = 1
missing_numbers = []

for num in numbers:
    while expected_num < num:
        missing_numbers.append(expected_num)
        expected_num += 1
    expected_num += 1

if len(missing_numbers) == 0:
    print("There are no missing numbers")

elif len(missing_numbers) == 1:
    print(f"The missing number is: {missing_numbers[0]}")

else:
    numbers_str = ", ".join(map(str, missing_numbers))
    print(f"The missing numbers are: {numbers_str}")


