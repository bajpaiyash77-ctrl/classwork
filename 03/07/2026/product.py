'''10 product with name and price in tuple format'''

products = [
    ("Product 1", 10.99),
    ("Product 2", 20.99),
    ("Product 3", 30.99),
    ("Product 4", 49990.99),
    ("Product 5", 50.99),
    ("Product 6", 60.99),
    ("Product 7", 70.99),
    ("Product 8", 80.99),
    ("Product 9", 90.99),
    ("Product 10", 100.99)
]

#display the products in tuple format
tuple1 = tuple(products)
print("Products in tuple format:")
for product in tuple1:
    print(product)

#Products with highest and lowest price
highest=max(tuple1)
print("Product with highest Price:",highest)

lowest=min(tuple1)
print("Product with lowest Price:",lowest)

#Count the number of products with price greater than 4000 along with their names
count = 0
for product in tuple1:
    if product[1] > 4000:
        count += 1
        print("Product with price greater than 4000:", product[0], "Price:", product[1])
print("Number of products with price greater than 4000:", count)

