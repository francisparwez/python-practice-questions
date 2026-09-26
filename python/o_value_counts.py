values = ["A", "B", "A", "C", "B", "A"]

def value_counts(values):
    count = {}
    
    for a in values:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    
    return count

print(value_counts(values))