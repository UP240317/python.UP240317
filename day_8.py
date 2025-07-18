# 1. Crear un diccionario vacío llamado dog
dog = {}

# 2. Agregar claves al diccionario dog
dog['name'] = 'Firulais'
dog['color'] = 'Marrón'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

print("Diccionario dog:", dog)
# 3. Crear el diccionario student con varias claves
student = {
    'first_name': 'Axel',
    'last_name': 'Campos',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'Excel'],
    'country': 'Mexico',
    'city': 'Guadalajara',
    'address': 'Calle Falsa 123'
}

# 4. Obtener la longitud del diccionario
print("Longitud del diccionario student:", len(student))

# 5. Obtener el valor de 'skills' y verificar su tipo
skills_value = student['skills']
print("Skills:", skills_value)
print("Tipo de skills:", type(skills_value))  # Debe ser list

# 6. Modificar skills (agregar uno o dos más)
student['skills'].append('SQL')
student['skills'].extend(['HTML', 'CSS'])
print("Nuevas skills:", student['skills'])

# 7. Obtener las claves como lista
keys_list = list(student.keys())
print("Claves del diccionario:", keys_list)

# 8. Obtener los valores como lista
values_list = list(student.values())
print("Valores del diccionario:", values_list)

# 9. Convertir diccionario a lista de tuplas con items()
items_list = list(student.items())
print("Diccionario como lista de tuplas:", items_list)

# 10. Eliminar un ítem del diccionario (por ejemplo, 'marital_status')
del student['marital_status']
print("Diccionario después de eliminar marital_status:", student)

# 11. Eliminar por completo el diccionario dog
del dog
# print(dog)  # Esto causaría un error si se descomenta
