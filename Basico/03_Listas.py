# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [30, 320, 34, 67, 45]

print(my_list)
print(len(my_list))

my_other_list = [18, 1.75, "Diego", "Galvis"]
print(type(my_other_list))

age, height, name, surname = my_other_list
print(name)


my_other_list.append("Ramirez Isaac")
print(my_other_list)

my_other_list.insert(1, "Gris")
print(my_other_list)

my_other_list.remove("Gris")
print(my_other_list)

my_list.pop()
print(my_list)

my_list = "Hola Python"
print(my_list)
print(type(my_list))

# del elimina un elemento concreto que nosotros le indiquemos
# sort ordena de mayor a menor los objetos de una lista