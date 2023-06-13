import csv

with open(file="dogs_are_awesome.csv", mode="r", encoding="utf=8") as my_file:
    csv_reader = csv.reader(my_file, delimiter=" ")
    for row in csv_reader:
        print(row)

with open(file="hello.csv", mode="w") as my_file:
    csv_writer = csv.writer(my_file)
    csv_writer.writerow("Hello")