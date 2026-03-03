# Lists Slicing
# Complete the list operations

# Create lists
numbers = ['a', 'b', 'c']  # Create list with 'a', 'b', 'c'

# List operations
answer_1 = numbers[1]  # Access the second element
answer_2 = numbers[-2]  # Access second from the end
answer_3 = numbers[1:3]  # Slice 1..3

# List modification
numbers[0] = 'z'
answer_4 = ['z', 'b', 'c'] # Predict numbers list after the change

# List operations
bonus = numbers + ['e']
numbers[0] = 'x'

answer_5 = ['x', 'b', 'c'] # Predict numbers now
answer_6 = ['z', 'b', 'c', 'e']  # Predict bonus now


