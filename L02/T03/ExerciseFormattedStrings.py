# Formatted Strings Exercise
# Predict what each will print, then write an f-string version

# What will these output?
# answer_1 is "Hello {}, your balance is {}.".format("Cindy", 50)
answer_1 = "Hello Cindy, your balance is 50."

# answer_2 is "Hello {0}, your balance is {1}.".format("Cindy", 50)
answer_2 = "Hello Cindy, your balance is 50."

# answer_3 is "Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50)
answer_3 = "Hello Cindy, your balance is 50."

# Now rewrite the SAME sentence using an f-string
# Output should be: "Hello Cindy, your balance is 50."
name = 'Cindy'
amount = 50
f_string_version = f"Hello {name}, your balance is {amount}."
