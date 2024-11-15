my_dict = {"audi": 305, "bmw": 265, "mercedes": 142}
print(my_dict)
print(my_dict["audi"])
print(my_dict.get("bmw"))
print(my_dict.setdefault("mercedes"))
print(my_dict.get("cooper", "Такого ключа нет"))
my_dict.update({"toiota": 427,
                "subary": 523})
print(my_dict)
a = my_dict.pop("audi")
print(a)
print(my_dict)
my_set = {1, 1, 1, 2, 3, 4, 4, 3, 2, 2, 3, 6, 7, "copybook", "pen", ("friends", 12, True)}
print(my_set)
my_set.update([23.5, "Anton"])
my_set.discard("copybook")
my_set.remove(("friends", 12, True))
print(my_set)
