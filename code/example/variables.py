# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Example
name = "deo40"
price = 12.50
availability = True
quantity = 1000
release = "2022-01-01"


def increase_price(amount):
    global price
    price += amount


increase_price(10)
print(price)
