values = [10, 12, 11, 13, 12, 15, 14, 100, 11, 13]

def median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    else:
        return lst[mid]

def remove_outliers_iqr_method(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    
    if n == 0 : return None
    
    mid = n // 2
    
    if n % 2 == 0:
        lower_half = numbers[:mid]
        upper_half = numbers[mid:]
    else:
        lower_half = numbers[:mid]
        upper_half = numbers[mid + 1:]
    
    q1 = median(lower_half)
    q3 = median(upper_half)
    
    iqr = q3 - q1
    
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr
    
    normal_values = []
    outliers = []
    
    for value in numbers:
        if value < lower_limit or value > upper_limit:
            outliers.append(value)
        else:
            normal_values.append(value)

    return normal_values, outliers

print(remove_outliers_iqr_method(values))

values = [50, 60, 70, 80, 89685, 88, 91, 102, 111]
print(remove_outliers_iqr_method(values))