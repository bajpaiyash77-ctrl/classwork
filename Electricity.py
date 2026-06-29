'''Electricity Bill Calculator'''
#input units consumed by given number of customers
num_customers = int(input("Enter the number of Houses: "))
#to calculate and display average electricity unit consumption for each customer, total electricity unit  for all customers, and the customer with the highest electricity unit consumption, and the customer with the lowest electricity unit consumption
total_units = 0
highest_units = 0
lowest_units = float('inf')
for i in range(num_customers):
    units = float(input(f"Enter the electricity units consumed by customer {i + 1}: "))
    total_units += units
    if units > highest_units:
        highest_units = units
    if units < lowest_units:
        lowest_units = units

print(f"Total electricity units consumed by all customers: {total_units}")
print(f"Average electricity units consumed per customer: {total_units / num_customers}")
print(f"Customer with the highest electricity units consumption: {highest_units}")
print(f"Customer with the lowest electricity units consumption: {lowest_units}")
