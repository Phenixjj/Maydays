import csv
from faker import Faker

fake = Faker()

# Generate data for 10 employees
employees = []
for _ in range(10):
    name = fake.name()
    salary = fake.random_int(min=20000, max=100000)
    employees.append((name, salary))

# Save data to CSV file
filename = 'employees.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Salary'])
    writer.writerows(employees)

print(f"CSV file '{filename}' generated successfully.")