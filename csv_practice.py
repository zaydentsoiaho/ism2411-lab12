import csv 
from datetime import datetime

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

# Exercise 5: Write orders with totals greater than $100 
print("\nExercise 5")

original_count = 0 
written_count = 0 

with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader: 
            original_count += 1
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
                written_count += 1

print(f"Wrote {written_count} rows out of {original_count} original rows.")

#Exercise 6: Read columns by name using DictReader. 
# csv.reader is useful for simple files when I know the column positions.
# DictReader is useful with headers because column names make the code clearer.

print("\nExercise 6")

dict_total_revenue = 0 


with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total_revenue += total 

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${dict_total_revenue:.2f}")


# Exercise 7: Summarize revenue by product. 
print("\nExercise 7")

summary = {}

with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity 

        summary[product] = summary.get(product,0) + total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# Exercise 8: Append the date, time, and the total revenue to a log. 
print("\nExercise 8")

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{datetime.now()} - Total revenue: ${total_revenue:.2f}\n")

print("Added one entry to data/run_log.txt.")