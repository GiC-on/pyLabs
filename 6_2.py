inp = input("Enter cities' names:\n")
lst = inp.split(" ")

if not("Москва" in lst):
    lst.append("Москва")

kort = tuple(lst)

print(kort)

input()
