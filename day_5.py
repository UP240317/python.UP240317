# 1. Lista vacía
empty_list = []

# 2. Lista con más de 5 elementos
my_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

# 3. Longitud de la lista
print(len(my_list))

# 4. Primer, medio y último elemento
print(my_list[0])
print(my_list[len(my_list) // 2])
print(my_list[-1])

# 5. Lista con datos variados
mixed_data_types = ['Axel', 25, 1.75, 'Soltero', 'CDMX']

# 6. Lista de empresas
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Imprimir lista
print(it_companies)

# 8. Número de compañías
print(len(it_companies))

# 9. Primera, media y última empresa
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

# 10. Modificar una empresa
it_companies[1] = 'Alphabet'

# 11. Agregar una empresa
it_companies.append('Tesla')

# 12. Insertar en el medio
it_companies.insert(len(it_companies)//2, 'Spotify')

# 13. Cambiar a mayúsculas (sin modificar IBM)
it_companies[0] = it_companies[0].upper()

# 14. Unir con '#; '
joined = '#; '.join(it_companies)
print(joined)

# 15. Verificar existencia
print('Google' in it_companies)
print('Alphabet' in it_companies)

# 16. Ordenar alfabéticamente
it_companies.sort()

# 17. Invertir orden
it_companies.reverse()

# 18. Cortar primeras 3 empresas
print(it_companies[:3])

# 19. Cortar últimas 3 empresas
print(it_companies[-3:])

# 20. Empresa del medio
middle_index = len(it_companies) // 2
print(it_companies[middle_index:middle_index+1])

# 21. Eliminar primera empresa
it_companies.pop(0)

# 22. Eliminar del medio
it_companies.pop(len(it_companies)//2)

# 23. Eliminar última
it_companies.pop()

# 24. Eliminar todas
it_companies.clear()

# 25. Destruir la lista
del it_companies

# 26. Unir frontend y backend
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27. Insertar Python y SQL después de Redux
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

# Nivel 2 - Lista de edades
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Ages ordenadas:", ages)

# Mínimo y máximo
print("Edad mínima:", min(ages))
print("Edad máxima:", max(ages))

# Agregar min y max nuevamente
ages.append(min(ages))
ages.append(max(ages))

# Mediana
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2] + ages[n//2 - 1]) / 2
else:
    median = ages[n//2]
print("Mediana:", median)

# Promedio
average = sum(ages) / len(ages)
print("Promedio:", average)

# Rango
age_range = max(ages) - min(ages)
print("Rango:", age_range)

# Comparar distancia con promedio
print("Distancia min-promedio:", abs(min(ages) - average))
print("Distancia max-promedio:", abs(max(ages) - average))

# Lista de países
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# País del medio
mid = len(countries) // 2
print("País del medio:", countries[mid])

# Dividir en dos mitades
first_half = countries[:mid+1]  # Si es impar, una más para la primera mitad
second_half = countries[mid+1:]
print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)

# Desempaquetar
c1, c2, c3, *scandic_countries = countries
print("Primeros tres países:", c1, c2, c3)
print("Países escandinavos:", scandic_countries)
