# Create a template string with {} placeholders for product and price
template1 = "The {} costs ${}."

# Test the template with different values
result1 = template1.format("laptop", 999)
result2 = template1.format("keyboard", 49)

# Create a template string with {0} and {1} positional indexes
# The template should repeat {0} at the end to show the customer name twice
template2 = "{0} placed order #{1}. Thank you, {0}!"

# Test the template with different values
result3 = template2.format("Sarah", 12345)
result4 = template2.format("John", 67890)

# Create a template string with named placeholders {item}, {qty}, and {total}
template3 = "Item: {item}, Quantity: {qty}, Total: ${total}"

# Test the template with different values
result5 = template3.format(item="mouse", qty=3, total=45)
result6 = template3.format(item="cable", qty=5, total=25)

# Create an f-string with variables
username = "Alex"
score = 87
result7 = f"{username} scored {score} points."

# Create f-string with an expression
length = 10
width = 5
result8 = f"Area: {length * width} square meters"
