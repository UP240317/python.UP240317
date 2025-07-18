# -------- LEVEL 1 --------

# 1. Crear una tupla vacía
empty_tuple = ()

# 2. Crear tuplas con nombres de hermanos y hermanas
sisters = ('Ana', 'Luisa')
brothers = ('Carlos', 'Miguel')

# 3. Unir hermanos y hermanas en una tupla siblings
siblings = sisters + brothers

# 4. ¿Cuántos hermanos tengo?
num_siblings = len(siblings)
print("Número de hermanos:", num_siblings)  # Salida: 4

# 5. Agregar padre y madre a la tupla y asignarla a family_members
family_members = siblings + ('Papá', 'Mamá')
print("Miembros de la familia:", family_members)

# -------- LEVEL 2 --------

# 6. Desempaquetar hermanos y padres
*siblings_unpack, father, mother = family_members
print("Hermanos:", siblings_unpack)
print("Padre:", father)
print("Madre:", mother)

# 7. Crear tuplas de alimentos
fruits = ('manzana', 'banana', 'naranja')
vegetables = ('zanahoria', 'brócoli', 'lechuga')
animal_products = ('leche', 'huevo', 'queso')

# Unirlas en una sola tupla
food_stuff_tp = fruits + vegetables + animal_products
print("Tupla de alimentos:", food_stuff_tp)

# 8. Convertir la tupla en una lista
food_stuff_lt = list(food_stuff_tp)
print("Lista de alimentos:", food_stuff_lt)

# 9. Extraer el elemento o elementos del medio
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index-1:middle_index+1]
else:
    middle_items = [food_stuff_lt[middle_index]]
print("Elemento(s) del medio:", middle_items)

# 10. Extraer los primeros 3 y últimos 3 elementos
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("Primeros tres:", first_three)
print("Últimos tres:", last_three)

# 11. Eliminar completamente la tupla food_stuff_tp
del food_stuff_tp
# print(food_stuff_tp)  # Esto daría error porque ya se eliminó

# 12. Verificar si un elemento está en una tupla
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("¿Estonia es un país nórdico?", 'Estonia' in nordic_countries)
print("¿Iceland es un país nórdico?", 'Iceland' in nordic_countries)


