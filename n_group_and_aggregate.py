sales = [
    ("Karachi", 1000),
    ("Lahore", 1500),
    ("Karachi", 2000),
    ("Islamabad", 1200),
    ("Lahore", 500),
    ("Karachi", 700)
]


def group_and_aggregrate(data):
    total = {}
    
    for city, amount in data:
        if city in total:
            total[city] += amount
        else:
            total[city] = amount
        
    return total


print(group_and_aggregrate(sales))