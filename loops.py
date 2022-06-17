# the for loop
# Note: The for loop does not require an indexing variable to set beforehand.

# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String
for x in "banana":
    print(x)

# The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# THE range() FUNCTION
for x in range(6):
  print(x)

# Using the start parameter:
for x in range(2, 6):
  print(x)

# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

