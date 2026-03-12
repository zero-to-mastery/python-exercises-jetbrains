# List Methods Exercise

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove "Banana" from the list
basket.remove("Banana")

# Remove "Blueberries" from the list
basket.remove("Blueberries")

# Put "Kiwi" at the end of the list
basket.append("Kiwi")

# Add "Apples" at the beginning of the list
basket.insert(0, "Apples")

# Count how many apples are in the basket
apple_count = basket.count("Apples")

# You could also use basket.clear() to empty the basket,
# but let’s not do that here so we can check the result.