# Sets Exercise

## Real-World Problem: Attendance Tracking

This exercise demonstrates a practical use of sets - finding missing elements by comparing two collections. This pattern appears frequently in real applications:
- Tracking who hasn't responded to an invitation
- Finding missing items in inventory
- Identifying unprocessed records
- Detecting absent students (as in this exercise)

## The Scenario

You have:
- A **set** of all students enrolled in the school
- A **list** of students who attended class today

Your goal: Find which students missed class.

## Set Difference in Action

The **difference** operation is perfect for this:
```python
all_students = {'Alice', 'Bob', 'Charlie'}
attended = {'Alice', 'Charlie'}
missed = all_students.difference(attended)  # Returns {'Bob'}
```

This finds elements in the first set that aren't in the second.

## Working with Different Data Types

Notice the attendance is a **list**, not a set. You'll need to convert it to a set before performing set operations. Python makes this easy:
```python
set(my_list)  # Converts list to set
```

## Your Task

Complete the attendance checker:
1. Convert the attendance list to a set
2. Use set difference to find who missed class
3. Store the result for printing

**Challenge:** Why is set difference more efficient than checking each student individually with a loop?
