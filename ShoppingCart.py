'''Shopping Cart Billing System'''
# input number of items
num_items = int(input("Enter the number of items in the shopping cart: "))

#while loop to input details for each item and display individual item cost, total bill amount, and most expensive and cheapest item and average cost of items
total_cost = 0
highest_cost = 0
lowest_cost = float('inf')
most_expensive_item = ""
cheapest_item = ""
for i in range(num_items):
    item_name = input(f"Enter the name of item {i + 1}: ")
    item_quantity = int(input(f"Enter the quantity of {item_name}: "))
    item_price = float(input(f"Enter the price of {item_name}: "))

    individual_cost = item_quantity * item_price
    total_cost += individual_cost

    if individual_cost > highest_cost:
        highest_cost = individual_cost
        most_expensive_item = item_name

    if individual_cost < lowest_cost:
        lowest_cost = individual_cost
        cheapest_item = item_name
    
average_cost = total_cost / num_items if num_items > 0 else 0





print(f"\nTotal Cost: ${total_cost:.2f}")
print(f"Most Expensive Item: {most_expensive_item} (${highest_cost:.2f})")
print(f"Cheapest Item: {cheapest_item} (${lowest_cost:.2f})")
print(f"Average Cost: ${average_cost:.2f}")
