# Creating and calling Function

def my_function():
    print("Hello from "
          "a function")


my_function()


# Arguments
def my_function_with_arguments(first_name, last_name):
    print(first_name + " " + last_name)


my_function_with_arguments("Emil", "Refsnes")


# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Return Values

def my_function(x):
    return 5 * x


print(my_function(3))
