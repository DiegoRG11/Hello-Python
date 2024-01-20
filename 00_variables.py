# Variables

my_string_variable = "My String variable"
print(my_string_variable) 

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_varieble = True
print(my_bool_varieble)

# Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_varieble)
print("Este es el valor de:", my_bool_varieble)

# Funciones del sistema 
print(len(my_string_variable))

# Variables en una sola linea
name, surname, alias, age = "Diego", "Galvis", "ElMango", 18
print("Me llamo:", name, surname, "Mi edad es:", age, "Y mi alias es:", age)

# Inputs
# name = input('Cual es tu nombre? ')
# age = input('Cual es tu edad? ')
# print(name)
# print(age)

# Cambiamos su tipo
name = 35
age = "Diego"
print(name)
print(age)

# Forzamos el tipo
address: str = "Esta es mi direccion"
address = 32
print(type(address))

