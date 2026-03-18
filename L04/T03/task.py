# Exercise Extending List

class SuperList(list):

    # This changes how len() works for SuperList objects
    def __len__(self):
        return 1000

super_list1 = SuperList()  # create an empty SuperList
super_list1.append(5) # add 5 to super_list1

# len(super_list1) returns 1000, not 1, because __len__() is overridden

# Get the first item from super_list1
answer_1 = super_list1[0]

# Check if SuperList is a subclass of list
answer_2 = issubclass(SuperList, list)

# Check if list is a subclass of object
answer_3 = issubclass(list, object)
