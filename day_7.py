# Crear conjunto de empresas de tecnología
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Longitud del conjunto
print("Longitud:", len(it_companies))  # Ej: 7

# 2. Agregar 'Twitter'
it_companies.add('Twitter')
print("Después de agregar Twitter:", it_companies)

# 3. Insertar múltiples compañías
it_companies.update(['Tesla', 'Intel', 'HP'])
print("Después de agregar múltiples empresas:", it_companies)

# 4. Eliminar una compañía (por ejemplo 'HP')
it_companies.remove('HP')
print("Después de eliminar HP:", it_companies)

# 5. Diferencia entre remove y discard:
# - remove lanza error si el elemento no existe
# - discard NO lanza error
it_companies.discard('NoExiste')  # No lanza error
# it_companies.remove('NoExiste')  # Lanzaría error

#---------LEVEL 2 ----------#
# Definimos dos conjuntos
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 23, 25, 28}

# 1. Unión de A y B
union_AB = A.union(B)
print("Unión A ∪ B:", union_AB)

# 2. Intersección de A y B
intersection = A.intersection(B)
print("Intersección A ∩ B:", intersection)

# 3. ¿A es subconjunto de B?
print("¿A es subconjunto de B?", A.issubset(B))

# 4. ¿A y B son disjuntos?
print("¿A y B son disjuntos?", A.isdisjoint(B))

# 5. Unir A con B y B con A
print("A unido con B:", A.union(B))
print("B unido con A:", B.union(A))

# 6. Diferencia simétrica (elementos que están en A o B pero no en ambos)
symmetric_diff = A.symmetric_difference(B)
print("Diferencia simétrica A △ B:", symmetric_diff)

# 7. Eliminar completamente los conjuntos
del A
del B

#--------------LEVEL 3 --------------------#
# 1. Comparar longitud entre lista y conjunto
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)
print("Longitud de la lista:", len(ages))
print("Longitud del conjunto:", len(ages_set))  # Conjunto elimina duplicados

# 2. Diferencias entre tipos de datos:
# string: cadena de texto ('hola')
# list: colección ordenada y mutable [1, 2, 3]
# tuple: colección ordenada e inmutable (1, 2, 3)
# set: colección desordenada de elementos únicos {1, 2, 3}

# 3. Palabras únicas en una oración
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print("Número de palabras únicas:", len(unique_words))
print("Palabras únicas:", unique_words)
