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
#ejercicio 15
print(company[0])
#ejercicio 16
print(company[13])
#ejercicio 17
print(company[10])
#ejercicio 18
phrase1='Python'
phrase2='For'
phrase3='All'
X=(phrase1[0])
Y=(phrase2[0])
Z=(phrase3[0])
all_text=print(X+Y+Z)
#ejercicio 19
ph1='Coding'
ph2='For'
ph3='All'
a=(ph1[0])
b=(ph2[0])
c=(ph3[0])
all_text=print(a+b+c)
#ejercicio 20
print(company.index('c'))
#ejercicio 21
print(company.index('f'))
#ejercicio 22
print(company.index('l'))
#ejercicio 23
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
#ejercicio 24
print(sentence.rindex('because'))
#ejercicio 25
phrase_to_remove = 'because because because'
new_sentence = sentence.replace(phrase_to_remove, '')
print(new_sentence)
#ejercicio 26
position = sentence.find('because')
print(position)
#ejercicio 27
start = sentence.find('because because because')
end = start + len('because because because')
result = sentence[start:end]
print(result)
#ejercicio 28
textos='coding for all'
starts_with_coding = textos.startswith('coding')
print(starts_with_coding)
#ejercicio 29
ends_with_coding = textos.endswith('coding')
print(ends_with_coding)
#ejercicio 30
espacios=" Coding for all "
print(espacios.strip())
#ejercicio 31
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"

print(var1, "is", var1.isidentifier())  
print(var2, "is", var2.isidentifier())  
#Actividad 32
librerias = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
unidos= "las siguientes son librarias:%s" % (librerias)
print(unidos) 


#Actividad 33
print("I am enjoying this challenge. \n I just wonder what is next.")


#Actividad 34
print("\tname     \tage    \tcountry")
print("\tcity")
print("\tAsabeneh \t250 \tFinland")
print("\tHelsinki")


#ACtividad 35
radius = 10
area = 3.14 * radius ** 2
print("el area del circulo con un radio de: %d es: %.2f" %(radius,area))


#Actividad 36
a=8
b=6
print("{} + {} = {}".format(a,b,a+b) )
print("{} - {} = {}".format(a,b,a-b) )
print("{} x {} = {}".format(a,b,a*b) )
print("{} / {} = {:.2f}".format(a,b,a/b) )
print("{} % {} = {}".format(a,b,a%b) )
print("{} // {} = {}".format(a,b,a//b))
print("{} ** {} = {}".format(a,b,a**b))
#final
