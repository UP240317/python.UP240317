#ejercicio 1
w1='tirthy'
w2='days'
w3='of'
w4='python'
text=w1+''+w2+''+w3+''+w4

print(text)
#ejercicio 2
a1 = 'Coding'
b2 = 'For'
c3 = 'All'

texto = a1 + ' ' + b2 + ' ' + c3
print(texto) 
#ejercicio 3
company='coding for all'
#ejercicio 4
print(company)
#ejercicio 5
print ('numero de caracteres para "coding for all": ',(len(company)))
#ejercicio 6
print(company.upper())
#ejercicio 7
print(company.lower())
#ejercicio 8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#ejercicio 9
first_space=company.find('')
print(company[first_space + 1:])
#ejercicio 10
print('coding'in company)
print(company.find('coding'))
print(company.index('coding'))
#ejercicio 11
new_company=company.replace('coding','python')
print(new_company)
#ejercicio 12
texte='python for everyone'
new_texte=texte.replace('everyone','all')
print(new_texte)
#ejercicio 13
word = company.split(' ')
print(word)
#ejercicio 14
words="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
list_companies = words.split(' ')
print(list_companies)