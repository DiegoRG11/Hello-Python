# Strings

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

# Foramteo

name, surname, age = "Diego", "Galvis", 18

print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

Language = "python"
a, b, c, d, e, f = Language
print(a)
print(e)

# Division

Language_slice = Language[1:3]
print(Language_slice)

# Reversa

Reversed_Language = Language [::-1]
print(Reversed_Language)

# Funciones

print(Language.capitalize())
print(Language.upper())
print(Language.count("t"))
print(Language.isnumeric())
print(Language.lower())
print(Language.upper().isupper())
print(Language.startswith("py"))



