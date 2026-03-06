# Sets Exercise: School attendance

school = {'Bobby', 'Tammy', 'Jammy', 'Sally', 'Danny'}
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

# 1 Find the students who missed class (in school but NOT in attendance_list).
answer_1 = school.difference(attendance_list)

# 2 Find the students who were present (names that are in BOTH school and attendance_list).
answer_2 = school.intersection(attendance_list)

# 3 Make a set of all unique names from school and attendance_list together.
answer_3 = school.union(attendance_list)

# 4 Check if school and attendance_list have no names in common (True/False).
answer_4 = school.isdisjoint(attendance_list)