subjects = ["Data Modeling and Visualization", "Machine Learning", "Artificial Intelligence", "Big Data Analytics", "Python Programming Lab"]

# a) Display the list using for loop.
print("Subjects:")
for subject in subjects:
    print(subject)

# b) Display 2nd and 5th element of the list.
print("\n2nd and 5th subjects:")
print(subjects[1])
print(subjects[4])

# c) Display first 4 elements of the list using the range of indexes.
print("\nFirst 4 subjects:")
print(subjects[:4])

# d) Display last 4 elements of the list using the range of negative indexes.
print("\nLast 4 subjects:")
print(subjects[-4:])

# e) Display if "Python Programming Lab" is available in the List or not.
print("\nIs 'Python Programming Lab' available in the list?")
print("Python Programming Lab" in subjects)

# f) Demonstrate the working of append() and insert() function.
print("\nAdding 'Cloud Computing' to the list using append()")
subjects.append("Cloud Computing")
print(subjects)

print("\nInserting 'Cyber Security' at the 3rd position using insert()")
subjects.insert(2, "Cyber Security")
print(subjects)

# g) Demonstrate the working of remove() and pop() function.
print("\nRemoving 'Machine Learning' from the list using remove()")
subjects.remove("Machine Learning")
print(subjects)

print("\nRemoving last element from the list using pop()")
subjects.pop()
print(subjects)
