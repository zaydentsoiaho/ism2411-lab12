import csv 

# Exercise 1: sales.csv is in the data folder. 

# Exercise 2: Read and print all rows including the header 

with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Exercise 3: Skip the header and print it separately.

print("\nExercise 3")

with open("data/sales.csv", newline="") as file: 
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# Exercise 4: Calculate the new row's revenue and totals 

print("\nExercise 4")

total_revenue = 0 

with open("data/sales.csv", newline="") as file: 
    reader = csv.reader(file)
    next(reader)

    for row in reader: 
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity 
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")