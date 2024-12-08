import random


def password():
    namber = random.randint(3, 20)
    return namber


namber = password()
print(namber)

password()


def raschet():
    result = []
    for i in range(1, namber):
        if namber % i == 0:
            result.append([i, namber - i])
    return result


result = raschet()

raschet()


def strok():
    os_strok = ""
    for j in result:
        os_strok += str(j[0]) + str(j[1])
    return os_strok


os_strok = strok()
print(os_strok)

strok()
