import csv 

# Exercise 1: sales.csv is in the data folder. 

# Exercise 2: Read and print all rows including the header 

with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)