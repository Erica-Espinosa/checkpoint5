#EJERCICIO 1

mis_primos = ['Julian', 'Vanessa', 'Tatiana', 'Valentina', 'Sara']
for nombre in mis_primos:
    print(nombre)
    
    
#EJERCICIO 2

def suma (uno,dos,tres):
    return uno + dos + tres


result = suma(25,12,7) 
print(result) 

#EJERCICIO 3

suma = lambda uno,dos,tres :uno + dos + tres
print(suma (5, 3, 4))


#EJERCICIO 4
#primera opción 
nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

if nombre in lista_nombre:
    print ('la variable conincide con algún valor de la lista')
else:
    print ('la variable no conincide con nungún valor de la lista')

#segunda opción
for nombres in lista_nombre:
    if nombre in nombres:
        print ('la variable conincide con el valor de la lista')
    else:
        print (f'la variable: {nombre},  no conincide con el valor de la lista: {nombres}')