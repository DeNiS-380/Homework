immutable_var = ("book", 1, 2, 3, True)
print(immutable_var)
immutable_var += ("pen", 4, False)
print(immutable_var)
immutable_var *= 2
print(immutable_var)
immutable_var += [9, 8, 7],
print(immutable_var)
immutable_var[16][0] = 6
print(immutable_var)
#immutable_var[0]="copybook"
mutable_list = ["house ", 0, 5, True]
print(mutable_list)
mutable_list[0] = "job"
mutable_list += ("movement", 5, 0)
mutable_list.append("rest")
print(mutable_list)
mutable_list.remove(5)
print(mutable_list)
mutable_list.pop(1)
print(mutable_list)
mutable_list.insert(1, 3)
print(mutable_list)
