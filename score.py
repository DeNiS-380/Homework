grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_students = list(students)
my_students.sort()
#print(my_students)
grad_students = {my_students[0]: grades[0], my_students[1]: grades[1], my_students[2]: grades[2],
                 my_students[3]: grades[3], my_students[4]: grades[4]}
#print(grad_students)
a = sum(grades[0]) / len(grades[0])
b = sum(grades[1]) / len(grades[1])
j = sum(grades[2]) / len(grades[2])
k = sum(grades[3]) / len(grades[3])
s = sum(grades[4]) / len(grades[4])
#print(a, b, j, k, s)
grad_students[my_students[0]] = a
grad_students[my_students[1]] = b
grad_students[my_students[2]] = j
grad_students[my_students[3]] = k
grad_students[my_students[4]] = s
print(grad_students)
