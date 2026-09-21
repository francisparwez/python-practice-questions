numbers = [12, 45, 7, 89, 23, 89, 34, 56]

largest = None
secondLargest = None

for num in numbers:
    
    if largest is None or num > largest:
        secondLargest = largest
        largest = num        
    elif num != largest:
        if secondLargest is None or num > secondLargest:
            secondLargest = num

print(f"Largest: {largest}")
print(f"Second Largest: {secondLargest}")